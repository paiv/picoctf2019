#!/usr/bin/env python
import io
import sys


def solve():
    return eval64(input())


VERBOSE = 0

def trace(*args, **kwargs):
    if VERBOSE > 1: print(*args, file=sys.stderr, flush=True, **kwargs)


class Calc:
    def eval(self, s):
        p = Calc._Parser()
        tree = p.parse(s)
        return tree.eval()

    (Number, OpAdd, OpSub, OpMul, OpDiv, OpMod, OpXor, OpOr, OpAnd, Op_f, Op_x, Op_t, Op_r, Op_o) = range(14)

    _parse_ops = {'+': OpAdd, '-': OpSub, '*': OpMul, '/': OpDiv, '%': OpMod,
        '^': OpXor, '|': OpOr, '&': OpAnd,
        'f': Op_f, 'x': Op_x, 't': Op_t, 'r': Op_r, 'o': Op_o}

    class _Node:
        def __init__(self, type, value=None):
            self.type = type
            self.value = value

        def eval(self):
            base = 0x10000000000000000
            def _mo(x):
                x = x % base
                return x if (x < base // 2) else (x - base)

            if self.type == Calc.Number:
                return _mo(self.value)
            else:
                a, b = self.left.eval(), self.right.eval()
                if self.type == Calc.OpAdd:
                    return _mo(a + b)
                elif self.type == Calc.OpSub:
                    return _mo(a - b)
                elif self.type == Calc.OpMul:
                    return _mo(a * b)
                elif self.type == Calc.OpDiv:
                    return _mo(a // b) if b else a
                elif self.type == Calc.OpMod:
                    return _mo(a % b) if b else a
                elif self.type == Calc.OpXor:
                    return _mo(a ^ b)
                elif self.type == Calc.OpOr:
                    return _mo(a | b)
                elif self.type == Calc.OpAnd:
                    return _mo(a & b)
                elif self.type == Calc.Op_f:
                    return a
                elif self.type == Calc.Op_x:
                    return b
                elif self.type == Calc.Op_t:
                    return a
                elif self.type == Calc.Op_r:
                    return b
                elif self.type == Calc.Op_o:
                    return b
                else:
                    raise Exception('unhandled op {}'.format(self.type))

    class _Parser:
        def parse(self, s):
            si = io.BufferedReader(io.BytesIO(s.encode('utf-8')))

            def parse_node():
                state = 0
                sign = None
                val = None
                node = None

                while si.peek(1):
                    pos = si.tell()
                    x, = si.read(1)
                    x = chr(x)
                    # trace('state', state, 'at', pos, ':', repr(x), f'{ord(x):02x}')

                    if state == 0:
                        if x.isspace():
                            pass
                        elif x == '(':
                            node = parse_node()
                            state = 1
                        elif x == '-':
                            sign = -1
                            val = 0
                            state = 10
                        elif x.isdigit():
                            si.seek(-1, io.SEEK_CUR)
                            sign = 1
                            val = 0
                            state = 10
                        else:
                            raise Exception('state {}: unexpected char at {}: {}'.format(state, pos, x))

                    elif state == 1:
                        if x.isspace():
                            pass
                        elif x == ')':
                            return node
                        elif x in '+-*/%^|&fxtro':
                            left = node
                            node = Calc._Node(Calc._parse_ops[x])
                            node.left = left
                            node.right = parse_node()
                            state = 2
                        else:
                            raise Exception('state {}: unexpected char at {}: {}'.format(state, pos, x))

                    elif state == 2:
                        if x.isspace():
                            pass
                        elif x == ')':
                            return node
                        else:
                            raise Exception('state {}: unexpected char at {}: {}'.format(state, pos, x))

                    elif state == 10:
                        if x.isdigit():
                            val = val * 10 + int(x)
                        else:
                            si.seek(-1, io.SEEK_CUR)
                            return Calc._Node(Calc.Number, sign * val)

                    else:
                        raise Exception('unhandled state {}'.format(state))

                if state == 10:
                    return Calc._Node(Calc.Number, sign * val)

                raise Exception('unhandled state {}'.format(state))

            return parse_node()


def eval64(s):
    calc = Calc()
    return calc.eval(s)


def tests():
    cases = [
        ('2', 2),
        ('(2)', 2),
        ('((2))', 2),
        ('((2)+(2))', 4),
        ('((2)+((2)))', 4),
        ('( (2) + (2) )', 4),
        ('(2+2)', 4),
        ('(2*2)', 4),
        ('(2*3)', 6),
        ('(2* (-3))', -6),
        ('(4-3)', 1),
        ('(2-3)', -1),
        ('(4/2)', 2),
        ('(4/3)', 1),
        ('(4/0)', 4),
        ('(3 % 4)', 3),
        ('(12 % 4)', 0),
        ('(2 % 0)', 2),
        ('(3 ^ 7)', 4),
        ('(7 ^ 3)', 4),
        ('(8 ^ 0)', 8),
        ('(8 ^ 2)', 10),
        ('(3 | 7)', 7),
        ('(3 | 0)', 3),
        ('(3 & 7)', 3),
        ('(3 & 0)', 0),
        ('(123 f 53)', 123),
        ('(53 f 123)', 53),
        ('(123 x 53)', 53),
        ('(53 x 123)', 123),
        ('(123 t 53)', 123),
        ('(53 t 123)', 53),
        ('(123 r 53)', 53),
        ('(53 r 123)', 123),
        ('(123 o 53)', 53),
        ('(53 o 123)', 123),
    ]

    for s, x in cases:
        assert eval64(s) == x, '{} = {} (actual: {})'.format(s, x, eval64(s))


if __name__ == '__main__':
    # tests()
    print(solve())
