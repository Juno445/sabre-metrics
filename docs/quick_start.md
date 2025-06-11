# Quick Start

This guide shows how to compute Sabre-Metrics in Python.

```bash
pip install sabre-metrics  # after packaging to PyPI
```

Example usage:
```python
from sabre_metrics import (
    calculate_ats,
    calculate_tcs,
    calculate_rtv,
    calculate_wsps,
    calculate_wufs,
)

ats = calculate_ats([10, 12, 8], [2, 1, 3], [1, 2, 1])
tcs = calculate_tcs(15, 10, 5, 2)
rtv = calculate_rtv(ats, tcs)
wsps = calculate_wsps(50, 40, 2.0, 3.0)
wufs = calculate_wufs(4, 1, 120000, 5)
print(ats, tcs, rtv, wsps, wufs)
```

For more details on each metric see the documents in this `docs/` directory.
