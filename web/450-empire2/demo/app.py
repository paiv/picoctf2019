#!/usr/bin/env python
import sys
from jinja2 import Template


class Config:
    pass

def main(s='{{2+2}}'):
    c = Config()
    t = Template(s)
    return t.render(name='Bob', config=c)


if __name__ == '__main__':
    print(main(*sys.argv[1:]))
