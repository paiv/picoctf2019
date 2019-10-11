#!/usr/bin/env python

def solve():
    data = [
        106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
        0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
        0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o146, 0o62 ,
        '6' , 'a' , '8' , '9' , '8' , '1' , '5' , '1' ,
    ]

    def tr(x):
        return x if isinstance(x, str) else chr(x)

    flag = ''.join(map(tr, data))
    return 'picoCTF{{{}}}'.format(flag)


if __name__ == '__main__':
    print(solve())
