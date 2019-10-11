// gcc -m32 -O2 forky.c -o forky
#include <stdio.h>
#include <unistd.h>
#include <sys/mman.h>


int main(int argc, char const *argv[]) {

    int* mem = mmap(NULL, 4, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    // if (mem == MAP_FAILED) {
    //     return 1;
    // }

    int* p = &mem[0];
    *p = 0x3b9aca00;

    fork();
    fork();
    fork();
    fork();

    p = &mem[0];
    *p += 0x499602d2;
    p = &mem[0];
    int x = *p;

    // printf("x:%u (%d)\n", x, x);

    // unbuffered:
    char buf[200];
    int n = snprintf(buf, sizeof(buf), "x:%u (%d)\n", x, x);
    if (n > 0) {
        write(1, buf, n);
    }

    return 0;
}
