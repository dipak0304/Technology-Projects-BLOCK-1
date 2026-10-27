# 🧪 Task 4 — Network Latency & Bandwidth

## Background (Ethernet & Wi‑Fi on Pi 4 / Pi 5)

Both Pi 4 and Pi 5 include **Gigabit Ethernet** and **dual-band 802.11ac Wi‑Fi** ([Pi 4 specs](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)). Wired tests usually show **lower latency** and more stable **iperf3** throughput than Wi‑Fi.

Pi 5’s **RP1** chip increases **USB 3** bandwidth; heavy USB storage traffic can still interact with overall I/O on small boards. Network benchmarks depend on your **LAN**, server, and cable — not on 32- vs 64-bit OS except for small stack differences.

### 1️⃣ On the server machine:
```bash
iperf3 -s
```

### 2️⃣ On the Raspberry Pi:
```bash
iperf3 -c <server-ip>
ping <server-ip> -c 30
```

### 3️⃣ Record:
- Bandwidth
- Latency (min/avg/max)
- Packet loss

📁 Save:
- `results/iperf.txt`
- `results/ping.txt`
