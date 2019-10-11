#include <stdio.h>

char badChars;
int flag_size;
int* flag_index;
FILE* output;
char buffChar;
int remain;

int main(int argc, char const *argv[]) {
    badChars = 0;

    FILE* ffp = fopen("flag.txt", "r");
    if (!ffp) exit(1);

    flag_size = 0;
    fseek(ffp, 0, 2);
    flag_size = ftell(ffp);
    fseek(ffp, 0, 0);

    login();

    if (flag_size > 0xfffe) exit(1);

    flag = malloc(flag_size);
    if (fread(flag, 1, flag_size, ffp) <= 0) {
        exit(0);
    }

    int t = 0;
    flag_index = &t;
    output = fopen("output", "w");
    buffChar = 0;
    remain = 7;

    fclose(ffp);

    encode();

    fclose(output);

    if (badChars) {
        // err
    }
    else {
        // ok
    }

    return 0;
}
