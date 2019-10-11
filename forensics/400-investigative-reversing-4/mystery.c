#include <stdio.h>

char* flag;
int* flag_index;

char codedChar(int i, char x, char r) {
    return (r & 0xfe) | ((x >> i) & 1);
}

void encodeDataInFile(src, dst) {
    FILE* ifp = fopen(src, "ra");
    FILE* ofp = fopen(dst, "a");
    if (ifp == NULL) {
        exit(0);
    }

    char buf[1];
    int er = fread(buf, 1, 1, ifp);

    for (int i = 0; i < 2019; ++i) {
        fputc(buf[0], ofp);
        er = fread(buf, 1, 1, ifp);
    }

    for (int i = 0; i < 50; ++i) {
        if (i % 5 == 0) {
            for (int j = 0; i < 8; ++j) {
                char x = codedChar(j, flag[*flag_index], buf[0]);
                fputc(x, ofp);
                er = fread(buf, 1, 1, ifp);
            }
            ++(*flag_index);
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

    fclose(ofp);
    fclose(ifp);
}

void encodeAll() {
    char dst[] = "Item01_cp.bmp";
    char src[] = "Item01.bmp";

    for (char n = '5'; n > '0'; --n) {
        dst[5] = n;
        src[5] = n;
        encodeDataInFile(src, dst);
    }
}

int main(int argc, char const *argv[]) {
    char fbuf[50];
    int fi;

    flag = &fbuf[0];
    flag_index = &fi;

    FILE* ffp = fopen("flag.txt", "ra");
    int n = fread(flag, 50, 1, ffp);
    if (n != 50) {
        exit(0);
    }
    fclose(ffp);
    encodeAll();
    return 0;
}
