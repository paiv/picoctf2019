#!/usr/bin/env python
import base64
import zlib


def decode_cookie(payload):
    if payload.startswith('session='):
        payload = payload[8:]
    if payload.startswith('.'):
        return unzip(b64x(payload.split('.')[1]))
    else:
        return b64x(payload.split('.')[0])


def b64x(data):
    data += '=' * (-len(data) % 4)
    return base64.urlsafe_b64decode(data)


def unzip(data):
    return zlib.decompress(data)


if __name__ == '__main__':
    import sys
    print(decode_cookie(sys.argv[1]))
