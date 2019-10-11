// gcc -O2 trump.c -o trump
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>

int main(int argc, char const *argv[]) {
    if (argc < 2) {
        puts("usage: trump <program>");
        return 0;
    }
    sigset_t signal_set;
    sigaddset(&signal_set, SIGALRM);
    sigprocmask(SIG_BLOCK, &signal_set, NULL);
    char* prog = strdup(argv[1]);
    char* args[] = {prog, 0};
    execve(args[0], args, 0);
    free(prog);
    return 0;
}
