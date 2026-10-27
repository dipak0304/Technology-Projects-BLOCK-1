# Technology Projects BLOCK 1

Welcome! This repository is a student lab journal for an introductory technology curriculum at Roehampton. It covers Git and the CLI, computer hardware and digital logic, multi-language programming, and Raspberry Pi benchmarking.

## 📚 Learning goals

You will:

- Understand component-level computer hardware and low-level programming fundamentals.
- Practice digital logic and number systems with worked examples.
- Explore Assembly, C, C++, Python, and Scratch.
- Measure CPU, memory, I/O, network, and thermal performance on a Pi.
- Keep a technical notebook: objectives, procedure, evidence, and reflection.

## 📁 Repository structure

### Week 1 — `1.1_software/`

| Path | Purpose |
|------|---------|
| `01_intro_git/01_git_github.md` | Fork, clone, commit, push, pull request |
| `02_CLI/` | Terminal activities (`pwd`, files, `nano`, system and network info) |
| `03_github_sync/01_commit_push.md` | Day-to-day Git workflow on the journal |

### Week 2 — `1.2_logic/`

| Path | Purpose |
|------|---------|
| `01_computers/` | Hardware vs software, disassembly, components, Raspberry Pi, reflection |
| `02_number_systems/` | Base conversion, binary arithmetic, two’s complement, fixed point, limits |
| `03_truth_tables/` | Boolean logic and truth tables |

Written answers for Week 2 activities are filled in the corresponding `.md` files.

### Week 3 — `1.3_instructions/`

| Path | Purpose |
|------|---------|
| `00_environment.md` | Toolchain install and version checks |
| `01_assembly.md` … `05_scratch.md` | Checkpoint instructions |
| `asm/` | `add.s`, `hello_arm.s` |
| `c/main.c`, `cpp/main.cpp`, `python/script.py` | Checkpoint source code |
| `journal/` | Reflections for each checkpoint |
| `journal_programming.md` | Checkpoint index and commit tags |
| `screeshots/` | Environment and assembly evidence (as required) |
| `scratch/` | Scratch project export or screenshot |

### Week 4 — `1.4_benchmarking/`

| Path | Purpose |
|------|---------|
| `00_raspberry_pi_32bit_context.md` | Pi 4/5 specs, 32-bit OS limits, throttling, official links |
| `01_cpu.md` … `05_thermal.md` | Lab tasks (each includes hardware background) |
| `cpu_test.py`, `memory_test.py` | Helper scripts |
| `results/` | `system_info.txt` plus task outputs (`cpu.txt`, `memory.txt`, …) |
| `REPORT.md` | Summary report (update with your Pi measurements) |

### Shared evidence — `images/`

| Path | Purpose |
|------|---------|
| `computer.webp` | Computer hardware photo (used in `1.2_logic/01_computers/02_computer_disassembly.md`) |
| `code/c.png` | C checkpoint — `main.c` run, output **Result: 8** |
| `code/cpp.png` | C++ checkpoint — `main.cpp` run, output **Result: 8** |
| `code/python.png` | Python checkpoint — `script.py` run, output **Result: 8** |
| `README.md` | Checklist of other images still required for full submission |

Program screenshots (Week 3):

![C program output](images/code/c.png)

![C++ program output](images/code/cpp.png)

![Python script output](images/code/python.png)

## ✅ Journal progress (this fork)

| Area | Status |
|------|--------|
| Week 2 written work (logic, numbers, truth tables) | Complete in markdown |
| Week 3 C / C++ / Python source | In `1.3_instructions/c`, `cpp`, `python` |
| Week 3 C / C++ / Python run evidence | `images/code/c.png`, `cpp.png`, `python.png` |
| Computer photo | `images/computer.webp` |
| Assembly builds, disassembly, Scratch | Pending — see `journal/` and checkpoint `.md` files |
| CLI step screenshots | Pending — `images/CLI_step1.jpg` … `CLI_step6.jpg` |
| PC/Pi component photos | Pending — paths in `images/README.md` |
| Benchmarking on Raspberry Pi | Pending — replace placeholders in `1.4_benchmarking/results/` |

## 🧭 How to use this journal

1. Start in `1.1_software` and follow the numbered activity files. Commit after each task.
2. Work through `1.2_logic` in order; each file builds on the previous one.
3. In `1.3_instructions`, complete checkpoints 0–6, commit with the tags in `journal_programming.md`, and keep screenshots under `images/` or `screeshots/` as each activity specifies.
4. Finish in `1.4_benchmarking`: run tests on the Pi, save output to `results/`, and write up findings in `REPORT.md`.

Typical Git loop:

```bash
git pull
# edit files, run labs, add images
git add .
git commit -m "Meaningful message"
git push
```

When your lecturer asks for submission, open a pull request from your fork to **Roehampton/Technology-Projects-BLOCK-1** with a clear title (e.g. student ID and block).

---

Have a great learning journey! Keep the journal updated and review it before quizzes or project work.
