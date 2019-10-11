#include <stdio.h>

typedef int8_t i8;

//  [ a       ] [ b       ] [ c       ]
//  8  9  a  b  c  d  e  f  0  1  2  3

int asm3(int a, int b, int c) {
    int x = 0;
    // x = (a & 0xff0000) << 8;
    x |= (-(i8)(b >> 24)) & 0xff;
    x |= (b & 0xff0000) >> 8;
    x ^= (c & 0xffff);
    return x;
}

int main(int argc, char const *argv[]) {
    int x = asm3(0xd46c9935, 0xdfe28722, 0xb335450f);
    printf("x: 0x%x\n", x);
    return 0;
}
