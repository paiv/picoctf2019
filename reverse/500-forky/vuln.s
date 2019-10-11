[0x0000056a]> pdb
/ (fcn) main 148
|   int main (int argc, char **argv, char **envp);
|           ; var int32_t prot @ ebp-0x14
|           ; var int32_t flags @ ebp-0x10
|           ; var void*var_ch @ ebp-0xc
|           ; var int32_t var_8h @ ebp-0x8
|           ; arg int32_t arg_4h @ esp+0x4
|           0x00000566      8d4c2404       lea ecx, [arg_4h]
|           0x0000056a      83e4f0         and esp, 0xfffffff0
|           0x0000056d      ff71fc         push dword [ecx - 4]
|           0x00000570      55             push ebp
|           0x00000571      89e5           mov ebp, esp
|           0x00000573      53             push ebx
|           0x00000574      51             push ecx
|           0x00000575      83ec10         sub esp, 0x10
|           0x00000578      e8d3feffff     call sym.__x86.get_pc_thunk.bx
|           0x0000057d      81c3571a0000   add ebx, 0x1a57
|           0x00000583      c745ec030000.  mov dword [prot], 3
|           0x0000058a      c745f0210000.  mov dword [flags], 0x21     ; '!'
|           0x00000591      83ec08         sub esp, 8
|           0x00000594      6a00           push 0                      ; size_t offset
|           0x00000596      6aff           push 0xffffffffffffffff     ; int fd
|           0x00000598      ff75f0         push dword [flags]          ; int flags
|           0x0000059b      ff75ec         push dword [prot]           ; int prot
|           0x0000059e      6a04           push 4                      ; size_t length
|           0x000005a0      6a00           push 0                      ; void*addr
|           0x000005a2      e829feffff     call sym.imp.mmap           ; void*mmap(void*addr, size_t length, int prot, int flags, int fd, size_t offset)
|           0x000005a7      83c420         add esp, 0x20
|           0x000005aa      8945f4         mov dword [var_ch], eax
|           0x000005ad      8b45f4         mov eax, dword [var_ch]
|           0x000005b0      c70000ca9a3b   mov dword [eax], 0x3b9aca00 ; [0x3b9aca00:4]=-1
|           0x000005b6      e835feffff     call sym.imp.fork
|           0x000005bb      e830feffff     call sym.imp.fork
|           0x000005c0      e82bfeffff     call sym.imp.fork
|           0x000005c5      e826feffff     call sym.imp.fork
|           0x000005ca      8b45f4         mov eax, dword [var_ch]
|           0x000005cd      8b00           mov eax, dword [eax]
|           0x000005cf      8d90d2029649   lea edx, [eax + 0x499602d2]
|           0x000005d5      8b45f4         mov eax, dword [var_ch]
|           0x000005d8      8910           mov dword [eax], edx
|           0x000005da      8b45f4         mov eax, dword [var_ch]
|           0x000005dd      8b00           mov eax, dword [eax]
|           0x000005df      83ec0c         sub esp, 0xc
|           0x000005e2      50             push eax
|           0x000005e3      e865ffffff     call sym.doNothing
|           0x000005e8      83c410         add esp, 0x10
|           0x000005eb      b800000000     mov eax, 0
|           0x000005f0      8d65f8         lea esp, [var_8h]
|           0x000005f3      59             pop ecx
|           0x000005f4      5b             pop ebx
|           0x000005f5      5d             pop ebp
|           0x000005f6      8d61fc         lea esp, [ecx - 4]
\           0x000005f9      c3             ret
[0x0000056a]>
