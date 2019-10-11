
int main(int argc, char const *argv[]) {
    FILE* ifp = fopen("flag.txt", "r");
    char buf[26];
    int n = fread(buf, 26, 1, ifp);
    if (n <= 0) {
        exit(0);
    }

    FILE* ofp = fopen("mystery.png", "a");
    for (int i = 0; i < 6; i++) {
        fputs(buf[i], ofp);
    }
    for (int i = 6; i < 15; i++) {
        fputs(buf[i] + 5, ofp);
    }
    fputs(buf[15]-3, ofp);
    for (int i = 16; i < 26; i++) {
        fputs(buf[i], ofp);
    }

    fclose(ofp);
    fclose(ifp);
    return 0;
}
