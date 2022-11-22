"""Service for testing https://jsonplaceholder.typicode.com/"""

import cerberus
import pytest
import requests


@pytest.mark.parametrize('input_id, output_id',
                         [(1, 1),
                          (-1, -1),
                          (0, 0)])
@pytest.mark.parametrize('input_title, output_title',
                         [('foo', 'foo'),
                          ('', ''),
                          (100, 100),
                          ('&', '&')])
def test_create_resource(base_url, input_id, output_id, input_title, output_title):
    headers = {"Content-type": "application/json; charset=UTF-8"}
    data = {'title': input_title, 'body': 'bar', 'userId': input_id}

    res = requests.post(base_url + '/posts', json=data, headers=headers)
    assert res.json()['title'] == output_title
    assert res.json()['body'] == 'bar'
    assert res.json()['userId'] == output_id


def test_update_resource(base_url):
    res = requests.put(base_url + '/posts/1', data={'id': 1, 'title': 'foo555', 'body': 'bar', 'userId': 1})
    assert res.status_code == 200
    assert res.json()['id'] == 1
    assert res.json()['title'] == 'foo555'
    assert res.json()['body'] == 'bar'
    assert res.json()['userId'] == '1'


@pytest.mark.parametrize('input_title, output_title',
                         [('foo', 'foo'),
                          ('', ''),
                          (100, '100'),
                          ('&', '&')])
def test_patch_resource(base_url, input_title, output_title):
    res = requests.patch(base_url + '/posts/2', data={'title': input_title})
    assert res.json()['title'] == output_title


def test_count_all_resources(base_url):
    res = requests.get(base_url + "/posts")
    assert res.status_code == 200
    assert len(res.json()) == 100


def test_validate_json_schema_comments(base_url):
    res = requests.get(base_url + "/comments/1")

    schema = {
        "body": {"type": "string"},
        "email": {"type": "string"},
        "id": {"type": "number"},
        "name": {"type": "string"},
        "postId": {"type": "number"}
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)

