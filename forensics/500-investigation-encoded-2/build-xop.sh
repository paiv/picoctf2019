#!/bin/sh

nasm -f macho xop.S -o xop.o
ld -lSystem xop.o -o xop
rm xop.o
