section .text
global _main

_main:
.loo:
    mov ecx, dword [.x]
    mov edx, 0x66666667
    mov eax, ecx
    imul edx
    sar edx, 1
    mov eax, ecx
    sar eax, 0x1f
    sub edx, eax
    mov eax, edx
    mov edx, eax
    shl edx, 2
    add edx, eax
    mov eax, ecx
    sub eax, edx
    test eax, eax

    add dword [.x], 1
    cmp dword [.x], 0x31
    jle .loo
    ret

section .data
    .x: dd 0
