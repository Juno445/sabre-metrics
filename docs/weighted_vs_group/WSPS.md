# Weighted Scalability Performance Score (WSPS)

This metric places a stronger emphasis on resolution efficiency while still
accounting for ticket volume. It uses a non-linear weighting of each factor.

## Formula

```
WSPS = (Agent_Tickets / Team_Avg_Tickets)^0.7 *
       (Team_Avg_Resolution_Time / Agent_Resolution_Time)^1.3
```

Higher scores indicate an agent can handle increased workload without slowing
down.
