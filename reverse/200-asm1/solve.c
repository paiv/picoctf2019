#include <stdio.h>

int asm1(int n) {
    if (n <= 0x37a) {
        if (n == 0x345) {
            return n + 3;
        }
        return n - 3;
    }
    if (n == 0x5ff) {
        return n - 3;
    }
    return n + 3;
}

int main(int argc, char const *argv[]) {
    int x = asm1(0x345);
    printf("x: 0x%x\n", x);
    return 0;
}
