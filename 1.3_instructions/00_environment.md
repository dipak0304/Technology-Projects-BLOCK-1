## 🧱 Checkpoint 0 — Environment Setup (commit: `setup`)

**Goal**: Install toolchain and verify versions.

Run:
```bash
sudo apt update
sudo apt install -y build-essential gcc g++ binutils python3 python3-pip gdb
```
Record (screenshot) the outputs of:
```bash
gcc --version
g++ --version
as --version
ld --version
python3 --version
```
**Evidence to commit**: Create a folder named `screeshots\` and upload images showing what you have done.

**Status:** Toolchain install commands listed above; run on the Pi and save version screenshots to `screeshots/` (see `screeshots/README.md`). Source code for later checkpoints is prepared under `asm/`, `c/`, `cpp/`, and `python/`.