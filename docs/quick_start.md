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
)

ats = calculate_ats([10, 12, 8], [2, 1, 3], [1, 2, 1])
tcs = calculate_tcs(15, 10, 5, 2)
rtv = calculate_rtv(ats, tcs)
print(ats, tcs, rtv)
```

For more details on each metric see the documents in this `docs/` directory.
