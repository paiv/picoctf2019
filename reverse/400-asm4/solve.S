section .text
global _main

.asm4:
	push   ebp
	mov    ebp,esp
	push   ebx
	sub    esp,0x10
	mov    dword  [ebp-0x10],0x280
	mov    dword  [ebp-0xc],0x0
	jmp    .l27
.l23:
	add    dword  [ebp-0xc],0x1
.l27:
	mov    edx,dword  [ebp-0xc]
	mov    eax,dword  [ebp+0x8]
	add    eax,edx
	movzx  eax,byte  [eax]
	test   al,al
	jne    .l23
	mov    dword  [ebp-0x8],0x1
	jmp    .l138
.l51:
	mov    edx,dword  [ebp-0x8]
	mov    eax,dword  [ebp+0x8]
	add    eax,edx
	movzx  eax,byte  [eax]
	movsx  edx,al
	mov    eax,dword  [ebp-0x8]
	lea    ecx,[eax-0x1]
	mov    eax,dword  [ebp+0x8]
	add    eax,ecx
	movzx  eax,byte  [eax]
	movsx  eax,al
	sub    edx,eax
	mov    eax,edx
	mov    edx,eax
	mov    eax,dword  [ebp-0x10]
	lea    ebx,[edx+eax*1]
	mov    eax,dword  [ebp-0x8]
	lea    edx,[eax+0x1]
	mov    eax,dword  [ebp+0x8]
	add    eax,edx
	movzx  eax,byte  [eax]
	movsx  edx,al
	mov    ecx,dword  [ebp-0x8]
	mov    eax,dword  [ebp+0x8]
	add    eax,ecx
	movzx  eax,byte  [eax]
	movsx  eax,al
	sub    edx,eax
	mov    eax,edx
	add    eax,ebx
	mov    dword  [ebp-0x10],eax
	add    dword  [ebp-0x8],0x1
.l138:
	mov    eax,dword  [ebp-0xc]
	sub    eax,0x1
	cmp    dword  [ebp-0x8],eax
	jl     .l51
	mov    eax,dword  [ebp-0x10]
	add    esp,0x10
	pop    ebx
	pop    ebp
	ret

_main:
    push .s
    call .asm4
    ret

section .rodata
    .s db 'picoCTF_e341d', 0
