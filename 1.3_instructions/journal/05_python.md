# Python script — reflection

## Output

```text
Result: 8
```

Screenshot evidence:

![Python script run](../../images/code/python.png)

(Source: `1.3_instructions/python/script.py` — output **Result: 8**.)

## Interpretation vs compilation

**Compilation** (C/C++/assembly) translates source to machine code ahead of time; the CPU runs native instructions directly. **Interpretation** (typical CPython) parses source and executes bytecode in a virtual machine, with runtime type checks and dynamic dispatch. Python starts faster to edit-run but usually runs slower for tight numeric loops; C/C++ trade longer compile/link steps for maximum native speed. Same algorithm (`y = x + 3`), different execution pipelines.
