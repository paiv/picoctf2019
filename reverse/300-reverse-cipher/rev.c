#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
    FILE* fi = fopen("flag.txt", "r");
    FILE* fo = fopen("rev_this", "a");
    if (fi == NULL) {
        puts("No flag found");
    }
    if (fo == NULL) {
        puts("please run this on the server");
    }
    char buf[24];
    int n = fread(buf, 24, 1, fi);
    if (n <= 0) {
        exit(0);
    }
    for (int i = 0; i < 8; i++) {
        fputc(buf[i], fo);
    }
    for (int i = 8; i < 23; i++) {
        char x = buf[i] + (i % 2 ? -2 : 5);
        fputc(x, fo);
    }
    fputc(buf[23], fo);
    fclose(fo);
    fclose(fi);
    return 0;
}
