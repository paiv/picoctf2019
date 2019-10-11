#!/usr/bin/env python
import binascii
import itertools
import string
from decimal import Decimal as dec, getcontext


def solve(fn='ciphertext'):
    with open(fn) as f:
        data = f.read()
    data = dict([p[0].strip(), int(p[1])] for s in data.splitlines() if s for p in [s.split(':')])
    c = data['c'] = data['ciphertext (c)']
    e, n = data['e'], data['N']

    getcontext().prec = len(str(n))

    # m^e mod n == m^e
    m = round(dec(c) ** (dec(1) / e))

    s = binascii.unhexlify(f'{m:x}')
    print(s.decode('ascii'))


if __name__ == '__main__':
    solve()
