#!/usr/bin/env python
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse as modinv


def solve():
    N = 4966306421059967
    P = 73176001
    Q = 67867967
    E = 65537
    assert N == P * Q
    D = modinv(E, (P - 1) * (Q - 1))

    key = RSA.construct((N, E, D, P, Q))
    return key.exportKey().decode('ascii')



if __name__ == '__main__':
    print(solve())
