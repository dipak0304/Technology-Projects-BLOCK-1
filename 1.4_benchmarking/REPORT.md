# Benchmarking lab report

## Summary

This report compares CPU compute time, memory allocation, storage I/O, network latency/bandwidth, and thermals under load on the Raspberry Pi. **Re-run all commands on your Pi** and replace placeholder values in `results/` with your measured data before submission.

## CPU

The Python loop squaring integers stresses a single core in user space. Record execution time from `cpu_test.py`, idle temperature from `vcgencmd measure_temp`, and observe `%CPU` in `htop` during the run. Shorter times indicate faster computation; temperature should stay within normal Pi limits unless the case limits airflow.

## Memory

Allocating ten million random floats stresses the allocator and RAM bandwidth. Compare `free -h` before and after the allocation. Slower SD cards or swap use can inflate times if memory pressure triggers paging (unlikely on a Pi with sufficient RAM).

## Storage I/O

`dd` write/read tests measure sequential throughput to the boot medium. Direct flags reduce caching effects. Note write and read MB/s from `dd` output; microSD class and filesystem matter more than on SSD desktops.

## Network

`iperf3` reports TCP bandwidth to a server on the LAN; `ping` gives round-trip latency and loss. Wi-Fi vs Ethernet and router placement strongly affect results.

## Thermal / throttling

`stress --cpu 4` heats the SoC; monitoring with `vcgencmd measure_temp` shows whether cooling is adequate. Sustained high temperature may cause **throttling**, reducing CPU clock and benchmark scores.

## Conclusion

Benchmarks are only meaningful when the environment is documented (Pi model, OS version, cooling, network path). Use your committed `results/*.txt` files as evidence and update this report with your numbers and one paragraph of comparison to expectations for your hardware.
