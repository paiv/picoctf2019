#include <stdio.h>

char codedChar(int i, char x, char r) {
    return (r & 0xfe) | ((x >> i) & 1);
}

int main(int argc, char const *argv[]) {
    FILE* ffp = fopen("flag.txt", "r");
    FILE* ifp = fopen("original.bmp", "r");
    FILE* ofp = fopen("encoded.bmp", "a");

    char buf[1];
    int er = fread(buf, 1, 1, ifp);

    for (int i = 0; i < 723; ++i) {
        fputc(buf[0], ofp);
        er = fread(buf, 1, 1, ifp);
    }

    char flag[50];
    int n = fread(flag, 50, 1);
    if (n != 50) {
        exit(0);
    }

    for (int i = 0; i < 100; ++i) {
        if (i % 2 == 0) {
            for (int j = 0; i < 8; ++j) {
                char x = codedChar(j, flag[i/2], buf[0]);
                fputc(x, ofp);
                er = fread(buf, 1, 1, ifp);
            }
        }
        else {
            fputc(buf[0], ofp);
            er = fread(buf, 1, 1, ifp);
        }
    }

    while (er) {
        fputc(buf[0], ofp);
        er = fread(buf, 1, 1, ifp);
    }

    return 0;
}
