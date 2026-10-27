# 🧪 Task 5 — Temperature & Throttling Test

## Background (thermals & `vcgencmd`)

The SoC integrates temperature sensors read by **`vcgencmd measure_temp`**. Under load, firmware reduces clocks to stay near safe limits — default **`temp_limit` 85 °C** ([overclocking / thermal docs](https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/computers/config_txt/overclocking.adoc)). On **Pi 4**, ARM clocks are often reduced progressively between about **80 °C and 85 °C**.

**`vcgencmd get_throttled`** reports undervoltage and throttling history as a hex bitmask ([vcgencmd reference](https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/computers/os/graphics-utilities.adoc)). Example bits: **`0x2`** ARM frequency capped now; **`0x4`** currently throttled; **`0x20000`** / **`0x40000`** same events since boot.

Throttling lowers **CPU benchmark scores** — Task 5 links heat directly to Task 1 times.

### 1️⃣ Run a 30‑second stress test:
```bash
stress --cpu 4 --timeout 30
```

### 2️⃣ In another terminal, monitor temperature:
```bash
watch -n 2 vcgencmd measure_temp
```

(Optional) Save repeated measurements into a CSV.

Also log after stress:

```bash
vcgencmd get_throttled
```

📁 Save results in:
- `results/thermal.txt` or
- `results/temperature.csv`

**Interpretation:** If `get_throttled` is not `0x0`, explain which bits were set and whether a heatsink, fan, or open case would help ([cooling white paper](https://pip.raspberrypi.com/documents/RP-003608-WP)).
