#!/usr/bin/env python
import requests
import sys
from urllib.parse import urljoin


def solve(url='http://2019shell1.picoctf.com:37889'):
    req = requests.Session()

    data = {
        'user': 'guest',
        'pass': 'guest',
    }

    r = req.post(urljoin(url, '/index.php?file=login'), data=data)
    print(r, r.url, r.headers)
    print(r.text)


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
