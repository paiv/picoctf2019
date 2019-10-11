#include <stdio.h>

int asm2(int a, int b) {
    int x, y;
    x = b;
    y = a;
    do {
        x++;
        y += 0xf9;
    }
    while (y <= 0x3c75);
    return x;
}

int main(int argc, char const *argv[]) {
    int x = asm2(0x6, 0x24);
    printf("x: 0x%x\n", x);
    return 0;
}
