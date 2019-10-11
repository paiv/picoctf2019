#!/usr/bin/env python
import binascii
import decimal
import re
import socket
import sys
from decimal import Decimal as dec, getcontext
from Crypto.Util.number import inverse as modinv


VERBOSE = 1


def trace(*args, **kwargs):
    if VERBOSE: print(*args, file=sys.stderr, flush=True, **kwargs)


class Interact:
    class Error(Exception): pass

    def __init__(self, host, port=None):
        if port is None:
            host, port = host.split(':', 1)
        self.host = host
        self.port = port

    def __enter__(self):
        self.s = socket.create_connection((self.host, self.port))
        self.s.settimeout(5)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.s.close()

    def send(self, text):
        trace('> ', text)
        self.sendb((text + '\n').encode('utf-8'))

    def sendb(self, data):
        trace('> ', len(data), 'bytes', data[:80])
        self.s.send(data)

    def read(self, size=1):
        t = self.s.recv(size).decode('utf-8')
        if len(t) == 0:
            raise Interact.Error('connection closed')
        return t

    def waitfor(self, regex, flags=0):
        if isinstance(regex, str):
            regex = re.compile(regex, flags)

        buf = ''
        while not regex.search(buf):
            buf += self.read()
            self.buf = buf
            trace(repr(buf))

        trace(buf)
        return buf


def solve(host='2019shell1.picoctf.com:41419', port=None):
    flag_rx = re.compile(r'(picoCTF\{[^\}]+\})')

    with Interact(host, port) as ii:
        while True:
            try:
                ii.waitfor(r'#### NEW PROBLEM ####\n')
            except Interact.Error:
                trace(ii.buf)
                break

            data = dict()

            while True:
                s = ii.waitfor(r' : |FOLLOWING ####\n')
                if ':' in s:
                    na = s.split()[0]
                    xa = int(ii.waitfor(r'\n'))
                    data[na] = xa
                else:
                    wat = ii.waitfor(r'\n').strip()
                    break

            ii.waitfor(r'FEASIBLE\? \(Y\/N\):')

            wat = ''.join(sorted(data.keys())) + f'-{wat}'

            res = dict()

            if wat == 'pq-n':
                p, q = data['p'], data['q']
                res['n'] = p * q

            elif wat == 'np-q':
                n, p = data['n'], data['p']
                res['q'] = n // p

            elif wat == 'en-q':
                e, n = data['e'], data['n']
                decimal.getcontext().prec = len(str(n)) * 20
                a = n - (e + 1)
                b = a * a - 4 * n
                if b >= 0:
                    b = int(dec(b).sqrt())
                    q = (a - b) // 2
                    p = (a + b) // 2
                    if p * q == n:
                        res['q'] = q
                        res['p'] = p

            elif wat == 'pq-totient(n)':
                p, q = data['p'], data['q']
                e = (p - 1) * (q - 1)
                res['totient(n)'] = e

            elif wat == 'enplaintext-ciphertext':
                e, n, m = data['e'], data['n'], data['plaintext']
                c = pow(m, e, n)
                res['ciphertext'] = c

            elif wat == 'ciphertexten-plaintext':
                e, n, c = data['e'], data['n'], data['ciphertext']
                # m = pow(c, d, n)
                # res['plaintext'] = m

            elif wat == 'epq-d':
                e, p, q = data['e'], data['p'], data['q']
                d = modinv(e, (p - 1) * (q - 1))
                res['d'] = d

            elif wat == 'ciphertextenp-plaintext':
                e, n, p, c = data['e'], data['n'], data['p'], data['ciphertext']
                q = n // p
                d = modinv(e, (p - 1) * (q - 1))
                m = pow(c, d, n)
                res['plaintext'] = m

            else:
                raise Exception(wat)

            if res:
                ii.send('Y')
                ii.waitfor(r'WHAT YOU GOT\! ###\n')
                for _ in range(len(res)):
                    q = ii.waitfor(r': ').split(':')[0]
                    ii.send(str(res[q]))
            else:
                ii.send('N')

    x = res['plaintext']
    flag = binascii.unhexlify(f'{x:x}').decode('ascii')
    return flag


# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)
#
#
# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m


if __name__ == '__main__':
    print(solve())
