#include <stdio.h>

int main(int argc, char const *argv[]) {
    ...
    char flag[50];

    FILE* ffp = fopen("flag.txt", "r");
    if (fread(flag, 1, 18, ffp) <= 0) {
        exit(0);
    }

    return 0;
}
