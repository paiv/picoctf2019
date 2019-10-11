#include <stdio.h>

int flag_size;
int* flag_index;
FILE* output;
char buffChar;
int remain;

int matrix[] = {8, 0, 12, 8, 14, 20, 10, 34, 4, 44, 12, 48, 12, 60, 10, 72, 6,
    82, 16, 88, 12, 104, 12, 116, 10, 128, 8, 138, 14, 146, 14, 160, 16, 174,
    10, 190, 8, 200, 6, 208, 10, 214, 12, 224, 12, 236, 14, 248, 16, 262, 14, 278, 4, 292};

char secret[] = {184, 234, 142, 186, 58, 136, 174, 142, 232, 170, 40, 187, 184,
    235, 139, 168, 238, 58, 59, 184, 187, 163, 186, 226, 232, 168, 226, 184,
    171, 139, 184, 234, 227, 174, 227, 186, 128};

bool isValid(char x) {
    if (x >= 'a' && x <= 'z') {
        return 1;
    }
    if (x >= 'A' && x <= 'Z') {
        return 1;
    }
    return x == ' ' ? 1 : 0;
}

char lower(char x) {
    if (x >= 'A' && x <= 'Z') {
        return x + ('a' - 'A');
    }
    return x;
}

void save(int x) {
    buffChar |= x;

    if (remain == 0) {
        remain = 7;
        fputc(buffChar, output);
    }
    else {
        buffChar <<= 1;
        remain--;
    }
}

int getValue(int i) {
    // return (secret bits) [i]
}

void encode() {
    char x = '@';

    for(; *flag_index < flag_size; ++*flag_index) {
        x = flag[*flag_index];
        if (!isValid(x)) {
            exit(1);
        }

        if (x == ' ')  {
            x = 'z' + 1;
        }

        int k = x - 'a';
        int p = matrix[k*2 + 1];
        int q = p + matrix[k*2];

        for (int i = p; i < q; ++i) {
            save(getValue(i));
        }
    }

    while (reman != 7) {
        save(0);
    }
}

int main(int argc, char const *argv[]) {
    FILE* ffp = fopen("flag.txt", "r");
    if (!ffp) {
        exit(1);
    }

    fseek(ffp, 0, 2);
    flag_size = ftell(ffp);
    fseek(ffp, 0, 0);

    if (flag_size > 0xfffe) {
        exit(1);
    }

    char* flag = malloc(flag_size);
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

    return 0;
}
