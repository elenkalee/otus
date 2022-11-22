"""Service for testing: https://www.openbrewerydb.org/"""

import pytest
import requests

base_url = "https://api.openbrewerydb.org"


@pytest.mark.parametrize("pages", [0, 20, 21, 50])
def test_number_per_page(pages):
    """Number of breweries to return each call.
    Note: Default per page is 20. Max per page is 50."""

    res = requests.get(base_url + '/breweries?per_page=' + str(pages))
    assert len(res.json()) == pages


@pytest.mark.parametrize("pages", [51, 999])
def test_number_per_page_max(pages):
    """Number of breweries to return each call.
    Note: Default per page is 20. Max per page is 50."""

    res = requests.get(base_url + '/breweries?per_page=' + str(pages))
    assert len(res.json()) == 50


def test_number_per_page_default():
    """Number of breweries to return each call.
        Note: Default per page is 20. Max per page is 50."""
    res = requests.get(base_url + '/breweries?per_page')
    assert len(res.json()) == 20


@pytest.mark.parametrize("pages", [5, 16, 100])
def test_sort_desc(pages):
    """Sort the results by one or more fields.
    asc for ascending order
    desc for descending order
    Note: by_dist does not work with the sort filter since it is a filter of its own."""
    res = requests.get(
        'https://api.openbrewerydb.org/breweries?by_state=ohio&sort=type,name:desc&per_page=' + str(pages))
    values = []
    for i in res.json():
        values.append(i['name'].lower())

    assert values == sorted(values, reverse=True)


@pytest.mark.parametrize("pages", [5, 16, 100])
def test_sort_asc(pages):
    """Sort the results by one or more fields.
    asc for ascending order
    desc for descending order
    Note: by_dist does not work with the sort filter since it is a filter of its own."""
    res = requests.get(
        'https://api.openbrewerydb.org/breweries?by_state=ohio&sort=type,name:asc&per_page=' + str(pages))
    values = []
    for i in res.json():
        values.append(i['name'].lower())

    assert values == sorted(values, reverse=False)
