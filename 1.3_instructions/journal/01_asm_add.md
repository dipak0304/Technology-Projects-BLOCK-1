# Assembly add — reflection

## Registers and behavior

The program uses **r0** as a general-purpose register. It loads the immediate value 5 into r0, then adds 3 to r0, leaving **8** in r0. There is no `printf` or exit syscall in this minimal program, so when run as a normal Linux executable linked with default entry expectations, observable behavior depends on how the process is launched; the meaningful result is the final value in r0 after the `add` (8). Registers r1–r6 are unused here.

## Disassembly snippet (annotate after building on the Pi)

After `objdump -d add`, expect instructions similar to:

```text
    mov r0, #5        @ load immediate 5 into r0
    add r0, r0, #3    @ r0 := r0 + 3  (result 8)
```

Build on Raspberry Pi: `as add.s -o add.o && ld add.o -o add`, then paste your actual `add.disasm.txt` lines here and commit a screenshot of the build.
