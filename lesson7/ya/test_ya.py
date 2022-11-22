"""
pytest lesson7/ya/test_ya.py --url=https://ya.ru/sfhfhfhfhfhfhfhfh --status_code=404
pytest lesson7/ya/test_ya.py --url=https://mail.ru --status_code=200
"""

import requests


def test_status_code(base_url, status_code):
    res = requests.get(base_url)
    assert res.status_code == int(status_code)
