# Assembly hello — reflection

## Register roles

- **r0**: First argument to the kernel — file descriptor **1** (stdout) for `write`.
- **r1**: Second argument — address of the message buffer (`msg`).
- **r2**: Third argument — byte count **14** for `"Hello ARM Pi!\n"`.
- **r7**: Syscall number — **4** for `write`, then **1** for `exit`.

## `svc #0`

On Linux/ARM, **supervisor call 0** switches to kernel mode and dispatches the syscall whose number is in **r7**, using r0–r6 as arguments per the ARM Linux ABI. The kernel performs the operation (writing to stdout or terminating the process) and returns to user code when applicable.

## Screenshot

Place terminal output showing `Hello ARM Pi!` under `screeshots/asm-hello.png` after running on the Pi.
