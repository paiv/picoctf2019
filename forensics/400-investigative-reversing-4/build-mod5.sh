#!/bin/sh

nasm -f macho mod5.S -o mod5.o
ld -lSystem mod5.o -o mod5
rm mod5.o
