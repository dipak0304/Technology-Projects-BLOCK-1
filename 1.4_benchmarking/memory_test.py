import time

try:
    import numpy as np
except ImportError:
    print("numpy not installed; run: pip install numpy")
    raise SystemExit(1)

start = time.perf_counter()
a = np.random.rand(10_000_000)
end = time.perf_counter()
print("Memory allocation time:", end - start, "seconds")
print("Array nbytes:", a.nbytes)
