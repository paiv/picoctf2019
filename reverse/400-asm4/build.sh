#!/bin/sh

nasm -f macho solve.S -o solve.o
ld -lSystem solve.o -o app
rm solve.o
