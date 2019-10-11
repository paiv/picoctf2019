#!/usr/bin/env python


def solve(fn='mystery.png'):
    with open(fn, 'rb') as f:
        f.seek(-26, 2)
        data = f.read()

    flag = data[:6] + bytes((x - 5)for x in data[6:15]) + bytes((x + 3)for x in data[15:16]) + data[16:]
    return flag


if __name__ == '__main__':
    print(solve())
