# Raspberry Pi & 32-bit OS — background for benchmarking

This page summarises **official Raspberry Pi documentation** and product specs so you can interpret your Week 4 results. Record your own system details in `results/system_info.txt` (template below).

## Why “32-bit” matters in this lab

Many classroom Pis run **Raspberry Pi OS (32-bit)**. That image is a port of Debian (currently **Trixie** on current releases, or **Bookworm** on the legacy 32-bit line) built for broad compatibility across Pi models ([Pi OS downloads](https://www.raspberrypi.com/software/operating-systems/)).

Important points from Raspberry Pi’s [64-bit OS announcement](https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/):

| Topic | 32-bit Raspberry Pi OS on Pi 4 / Pi 5 |
|--------|----------------------------------------|
| CPU hardware | Pi 4 and Pi 5 use **64-bit ARM cores** (Cortex-A72 / Cortex-A76), even when the OS is 32-bit. |
| User programs | Run as **32-bit (AArch32 / armhf)** processes unless you use a 64-bit OS. |
| RAM on 8 GB Pi 4 | The board can use **up to 8 GB** of RAM with LPAE, but **each process** is limited to about **3 GB** of virtual address space (top 1 GB reserved for the kernel). |
| Performance | 64-bit builds can be faster in some benchmarks; 32-bit remains common in teaching because one image runs on more boards. |

For marking, always note **Pi model**, **RAM size**, **32- vs 64-bit OS**, and **OS version** next to your timings.

## Verify your environment (run on the Pi)

```bash
uname -m          # often armv7l on 32-bit OS; aarch64 on 64-bit OS
getconf LONG_BIT  # 32 or 64 (userspace width)
cat /proc/device-tree/model
free -h
vcgencmd version
```

Save the output to `results/system_info.txt`.

## Hardware reference (Pi 4 & Pi 5)

Specs below come from [Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/) and [Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) product pages. Your bench results should be compared to **your** model, not a different generation.

### Raspberry Pi 4 Model B

- **SoC:** Broadcom BCM2711, quad-core **Cortex-A72 (ARMv8)**, up to **1.8 GHz**
- **RAM:** 1 / 2 / 4 / 8 GB LPDDR4-3200
- **Network:** Gigabit Ethernet; dual-band **802.11ac** Wi‑Fi; Bluetooth 5.0
- **USB:** 2× USB 3.0, 2× USB 2.0
- **Storage:** microSD (OS and data); boot and I/O speed depend heavily on card quality
- **Video / GPU:** VideoCore VI; H.265/H.264 decode; OpenGL ES 3.1
- **Power:** 5 V via USB-C (recommended **3 A** supply; more if USB peripherals draw high current)
- **Ambient:** 0–50 °C (operating environment on the case)

### Raspberry Pi 5

- **SoC:** Broadcom BCM2712, quad-core **Cortex-A76 @ 2.4 GHz**
- **RAM:** 1 / 2 / 4 / 8 / 16 GB LPDDR4X-4267
- **I/O:** RP1 chip — faster USB and SD (SDR104 high-speed mode); optional **PCIe 2.0** via HAT
- **Network:** Gigabit Ethernet; dual-band Wi‑Fi; Bluetooth 5.0 / BLE
- **Power:** **5 V / 5 A** USB-C recommended for full performance

Pi 5 is **roughly two to three times faster** than Pi 4 in CPU-oriented work (vendor claim); your `cpu_test.py` time should reflect that if you upgrade hardware.

## How this maps to each benchmark task

| Task | Hardware / OS factor (32-bit lab) |
|------|----------------------------------|
| **CPU** | Clock speed, core count, throttling, and **armhf** code generation all affect loop time. Python on 32-bit still uses the same numeric loop, but the interpreter and libraries are 32-bit builds. |
| **Memory** | `numpy` allocation tests **RAM bandwidth and allocator**; on 32-bit OS, very large **single** arrays can hit virtual address limits sooner than on 64-bit OS (especially on 8 GB boards). |
| **Storage I/O** | microSD **class / UHS speed** dominates; Pi 5 improves SD throughput (SDR104). `dd` results are not comparable between Pi 4 and Pi 5 without noting the card and model. |
| **Network** | Gigabit Ethernet is shared with USB on Pi 4; Wi‑Fi adds latency vs wired. `iperf3` and `ping` depend on router, cable, and server — not CPU bitness alone. |
| **Thermal** | SoC temperature drives **frequency capping**. Use `vcgencmd measure_temp` and `vcgencmd get_throttled` ([vcgencmd docs](https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/computers/os/graphics-utilities.adoc)). |

## Temperature and throttling (Pi 4 family)

From Raspberry Pi [overclocking / thermal documentation](https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/computers/config_txt/overclocking.adoc):

- Default **`temp_limit`** is **85 °C** — above this, clocks voltages return toward defaults to protect the SoC.
- On **Pi 4**, between about **80 °C and 85 °C**, ARM cores are **progressively throttled**; at **85 °C**, GPU and ARM throttling increase.
- **`vcgencmd get_throttled`** returns a bitmask (e.g. undervoltage, ARM frequency capped, currently throttled). A return of **`throttled=0x0`** means none of those conditions are active at that instant.

Example monitoring during Task 5:

```bash
vcgencmd measure_temp
vcgencmd get_throttled
stress --cpu 4 --timeout 30
```

## Install lab tools (Debian / Raspberry Pi OS)

```bash
sudo apt update
sudo apt install -y python3 python3-pip htop stress-ng iperf3
pip3 install numpy --break-system-packages   # if apt numpy is unavailable; prefer: sudo apt install python3-numpy
```

On 32-bit OS, use **`python3`** and packages from the **armhf** repositories unless your lecturer specifies otherwise.

## `results/system_info.txt` template

Paste command output here when you start the lab:

```text
=== Model & OS ===
(Paste: cat /proc/device-tree/model, uname -a, getconf LONG_BIT)

=== Memory ===
(Paste: free -h)

=== Firmware ===
(Paste: vcgencmd version)

=== Notes ===
Pi model:
RAM:
32-bit or 64-bit OS:
SD card model (if known):
Cooling (none / heatsink / fan / case):
```

## Further reading (official)

- [Raspberry Pi OS downloads (32-bit and 64-bit)](https://www.raspberrypi.com/software/operating-systems/)
- [Raspberry Pi 4 specifications](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)
- [Raspberry Pi 5 product page](https://www.raspberrypi.com/products/raspberry-pi-5/)
- [Why Raspberry Pi OS moved to 64-bit (and 32-bit limits)](https://www.raspberrypi.com/news/raspberry-pi-os-64-bit/)
- [Cooling a Raspberry Pi (white paper PDF)](https://pip.raspberrypi.com/documents/RP-003608-WP)
