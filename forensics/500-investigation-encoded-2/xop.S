section .text
global _main


.encode:
    cmp byte [.x], 0x24
    je .done
    movsx eax, byte [.x]
    lea ecx, [eax + 0x12]
    mov edx, 0x38e38e39
    mov eax, ecx
    imul edx
    sar edx, 3
    mov eax, ecx
    sar eax, 0x1f
    sub edx, eax
    mov eax, edx
    shl eax, 3
    add eax, edx
    shl eax, 2
    sub ecx, eax
    mov edx, ecx
    mov ecx, edx
    sar ecx, 0x1f
    mov eax, edx
    xor eax, ecx
    sub eax, ecx
.done:
    nop
    ret

_main:
.loop:
    call .encode
    inc byte [.x]
    cmp byte [.x], 37
    jl .loop
    mov eax, 0
    ret

section .data
.x: dd 0
