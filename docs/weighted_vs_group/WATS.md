# Weighted Agent Time Score (WATS)

The Weighted Agent Time Score extends ATS by raising each average time
component to a configurable exponent before applying the usual weights.
This lets teams emphasize particular timing metrics.

```text
avg_res = mean(resolution_times)
avg_resp = mean(response_times)
avg_first = mean(first_response_times)

denominator = (avg_res ** res_weight) * 0.5 \
            + (avg_resp ** resp_weight) * 0.2 \
            + (avg_first ** first_weight) * 0.3
WATS = 100 / denominator
```

Weights must be non-negative and all input sequences must contain at
least one value.
