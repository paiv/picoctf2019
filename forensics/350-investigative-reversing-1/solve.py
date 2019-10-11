#!/usr/bin/env python


def solve(fn1='mystery.png', fn2='mystery2.png', fn3='mystery3.png'):
    def read_from_end(fn, n):
        with open(fn, 'rb') as f:
            f.seek(-n, 2)
            return f.read()

    a = read_from_end(fn1, 16)
    b = read_from_end(fn2, 2)
    c = read_from_end(fn3, 8)

    # c[0] = flag[1]
    # b[0] = flag[0] + f(flag[0])
    # c[1] = flag[2]
    # c[2] = flag[5]
    # a[0] = flag[4]

    # a[1] = flag[6]
    # ...
    # a[4] = flag[9]

    # b[1] = flag[3] + 4

    # c[3] = flag[10]
    # ...
    # c[7] = flag[14]

    # a[5] = flag[15]
    # ...
    # a[15] = flag[25]


    flag = (b'picoCT' +
        bytes(a[i+1] for i in range(4)) +
        bytes(c[i+3] for i in range(5)) +
        bytes(a[i+5] for i in range(11)) )

    return flag


if __name__ == '__main__':
    print(solve())
