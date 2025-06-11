# Weighted Total Revenue Impact (WTRI)

Weighted Total Revenue Impact adjusts the base TRI metric by applying
custom multipliers to each revenue loss component before dividing by the
number of SLA violations.

```text
weighted_total = (medium_loss * weight_medium)
                + (high_loss * weight_high)
                + (urgent_loss * weight_urgent)
WTRI = weighted_total / violations
```

All loss amounts, weights, and the violation count must be non-negative,
with `violations` greater than zero.
