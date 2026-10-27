# 🧪 Task 2 — Memory Allocation Test

## Background (RAM & 32-bit OS)

Pi 4 offers **1–8 GB LPDDR4**; Pi 5 offers **1–16 GB LPDDR4X** ([product pages](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)). **`free -h`** shows total RAM visible to the kernel.

On **32-bit Raspberry Pi OS**, the kernel can use LPAE to address more physical RAM on an 8 GB Pi 4, but **one process** typically cannot use more than about **3 GB** of virtual memory ([Pi 64-bit OS article](https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/)). Ten million `float64` values ≈ **76 MB** — well within limits, but the test still reveals **allocation speed** and memory pressure if other apps are open.

### 1️⃣ Run this Python script:
```python
import time, numpy as np
start = time.perf_counter()
a = np.random.rand(10_000_000)
end = time.perf_counter()
print('Memory allocation time:', end - start)
```

### 2️⃣ Check memory usage:
```bash
free -h
```

📁 Save results in `results/memory.txt`

**Interpretation:** Compare **used/available** before and after the script. On a 1 GB Pi, swapping to SD can slow allocation; on 32-bit OS, document RAM size and OS bitness when explaining anomalies.
