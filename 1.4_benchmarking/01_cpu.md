# 🧪 Task 1 — CPU Speed Test

## Background (Pi 4 / Pi 5, 32-bit OS)

The CPU is inside the Broadcom SoC (**BCM2711** on Pi 4: quad **Cortex-A72** up to **1.8 GHz**; **BCM2712** on Pi 5: quad **Cortex-A76** @ **2.4 GHz**). Even with **32-bit Raspberry Pi OS**, these cores run your Python interpreter as a 32-bit (`armhf`) process; the loop below is mostly **single-threaded integer work**, so you exercise one core heavily unless Python or the OS migrates threads.

Before timing, record `results/system_info.txt`. Shorter **execution time** = faster CPU *for this test*; compare only like-for-like (same Pi model, same OS bitness, similar temperature).

Sources: [Pi 4 specs](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/), [Pi 5 specs](https://www.raspberrypi.com/products/raspberry-pi-5/).

### 1️⃣ Run this Python script:
```python
import time

def cpu_stress(n=5_000_000):
    total = 0
    for i in range(n):
        total += i*i
    return total

start = time.perf_counter()
cpu_stress()
end = time.perf_counter()
print('Execution time:', end - start, 'seconds')
```

### 2️⃣ Record:
- Execution time
- CPU temperature:
```bash
vcgencmd measure_temp
```
- CPU usage in `htop`
- Optional: `cat /proc/cpuinfo | grep -E 'Model|Hardware|Revision'` and `getconf LONG_BIT` (32 vs 64 userspace)

📁 Save results in `results/cpu.txt`

**Interpretation:** If `vcgencmd get_throttled` shows frequency capping during the run, your CPU time includes thermal or power limits — note that in `REPORT.md`.
