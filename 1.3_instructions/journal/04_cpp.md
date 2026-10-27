# C++ program — reflection

## Output

Expected:

```text
Result: 8
```

Screenshot evidence:

![C++ program run](../../images/code/cpp.png)

(Source: `1.3_instructions/cpp/main.cpp` — output **Result: 8**.)

## C vs C++ binary (at a glance)

The C++ executable is often **slightly larger** than the C version because `iostream` pulls in more library code than `printf` alone, and name mangling / static initializers for streams may add sections. Disassembly may show calls into `std::ostream` machinery rather than a direct `printf` call. Both still compile to native ARM instructions; the difference is mostly **linked library surface**, not the arithmetic itself.
