# Benchmarking lab report

## System under test (complete from your Pi)

Fill this from `results/system_info.txt` and `00_raspberry_pi_32bit_context.md`:

| Field | Your value |
|-------|------------|
| Model (e.g. Pi 4 Model B / Pi 5) | |
| RAM | |
| OS | Raspberry Pi OS **32-bit** or **64-bit** (Debian version) |
| Kernel (`uname -r`) | |
| Userspace width (`getconf LONG_BIT`) | |
| Storage | microSD model / size |
| Cooling | none / heatsink / fan / case |
| Network path | Ethernet or Wi‑Fi |

**32-bit note:** On 32-bit OS, Pi 4/5 still use 64-bit ARM cores, but programs run as 32-bit processes; on an **8 GB** Pi 4, a **single process** is limited to about **3 GB** virtual memory ([Raspberry Pi blog](https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/)). This lab’s tests stay below that limit.

## Summary

This report compares CPU compute time, memory allocation, storage I/O, network latency/bandwidth, and thermals under load on the Raspberry Pi. Replace placeholder text with **your** measurements from `results/*.txt`.

## CPU

The Python loop in `cpu_test.py` stresses integer arithmetic on one core. **Pi 5** (Cortex-A76 @ 2.4 GHz) should finish faster than **Pi 4** (Cortex-A72 @ up to 1.8 GHz) under similar conditions ([specs](https://www.raspberrypi.com/products/raspberry-pi-5/)).

Record: execution time, idle `vcgencmd measure_temp`, `htop` CPU usage, and whether **`get_throttled`** was non-zero during the run.

*Your results:* (paste from `results/cpu.txt`)

## Memory

Ten million random floats test allocation and RAM bandwidth. Compare `free -h` before and after. Low RAM models (1 GB) may use swap on SD, which slows allocation.

*Your results:* (paste from `results/memory.txt`)

## Storage I/O

`dd` sequential tests reflect **microSD quality** and Pi generation (Pi 5 SDR104 vs Pi 4). Report write and read MB/s.

*Your results:* (paste from `results/io.txt`)

## Network

`iperf3` measures TCP throughput to a LAN server; `ping` measures RTT and loss. Gigabit Ethernet on Pi 4/5 is shared with USB on Pi 4 — note if you used Wi‑Fi.

*Your results:* (paste from `results/iperf.txt` and `results/ping.txt`)

## Thermal / throttling

`stress --cpu 4` heats the SoC. Between ~**80 °C and 85 °C** on Pi 4, ARM frequency may drop ([thermal documentation](https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/computers/config_txt/overclocking.adoc)). Log temperature over time and final **`vcgencmd get_throttled`**.

*Your results:* (paste from `results/thermal.txt` or summarise `temperature.csv`)

## Conclusion

In 1–2 paragraphs: How do your numbers compare to what you expect for your **model and 32-bit OS**? Did throttling or SD speed dominate any result? What would you change (cooling, wired network, better SD card, 64-bit OS) for a follow-up test?

## References

- [Raspberry Pi OS downloads](https://www.raspberrypi.com/software/operating-systems/)
- [Pi 4 Model B specifications](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)
- [Pi 5 product information](https://www.raspberrypi.com/products/raspberry-pi-5/)
- [Raspberry Pi OS 64-bit and memory limits](https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/)
- [vcgencmd / get_throttled](https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/computers/os/graphics-utilities.adoc)
