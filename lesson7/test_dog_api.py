"""Service fot testing: https://dog.ceo/dog-api/"""

import cerberus
import pytest
import requests


@pytest.mark.parametrize("link",
                         ["https://dog.ceo/api/breeds/list/all", "https://dog.ceo/api/breed/beagle/images/random",
                          "https://dog.ceo/api/breed/hound/list"])
def test_validate_json_with_schema(link):
    res = requests.get(link)
    print(res.json())
    schema = {
        "message": {},
        "status": {},
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)


@pytest.mark.parametrize("breed", ["borzoi", "labradoodle", "golden"])
def test_get_random_photo_by_breed(breed):
    res = requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")

    assert res.status_code == 200


@pytest.mark.parametrize("number_positive", [1, 17, 50])
def test_get_multiple_random_image_positive(number_positive):
    """Max number returned is 50. More info here: https://github.com/ElliottLandsborough/dog-ceo-api/pull/3"""
    response = requests.get("https://dog.ceo/api/breeds/image/random/" + str(number_positive))
    assert len(response.json()['message']) == number_positive
    assert response.status_code == 200


@pytest.mark.parametrize("number_negative", [-1, 0])
def test_get_multiple_random_image_negative(number_negative):
    """Max number returned is 50. More info here: https://github.com/ElliottLandsborough/dog-ceo-api/pull/3"""
    response_neg = requests.get("https://dog.ceo/api/breeds/image/random/" + str(number_negative))
    assert len(response_neg.json()['message']) == 1


@pytest.mark.parametrize("number_more_50", [51, 666])
def test_get_multiple_random_image_more_50(number_more_50):
    """Max number returned is 50. More info here: https://github.com/ElliottLandsborough/dog-ceo-api/pull/3"""
    response_more_50 = requests.get("https://dog.ceo/api/breeds/image/random/" + str(number_more_50))
    assert len(response_more_50.json()['message']) == 50


@pytest.mark.parametrize('incorrect_link',
                         ['http://dog.ceo/api/breeds/image/rando', "http://dog.ceo/api/bred/hound/afghan/images",
                          "http://dog.ceo/api/breed/beagle/imags/random"])
def test_get_error_for_wrong_get_request(incorrect_link):
    response = requests.get(incorrect_link)
    assert response.status_code == 404
    assert response.json()['status'] == 'error'
    assert response.json()['message'] == f'No route found for "GET {incorrect_link}" with code: 0'
