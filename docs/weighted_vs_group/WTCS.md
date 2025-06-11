# Weighted Ticket Complexity Score
## Abstract
"Technicians don't grow unless they're challenged. Some technicians will naturally seek out a challenge, but this prevents others from being given an opportunity to rise up and learn."

Traditional IT performance metrics often fail to account for the complexity and strategic value of work completed. By treating all tickets equally, organizations risk rewarding volume over impact and stifling growth. This document introduces Weighted Ticket Complexity Score (WTCS), a framework that quantifies the difficulty and importance of tasks to fairly evaluate technician performance. Like SABRmetrics in baseball, WTCS shifts the focus from superficial metrics (e.g., "tickets resolved") to nuanced, data-driven insights that reflect true contribution and potential.

## Introduction
Modern IT environments are dynamic and complex. A technician resolving 50 password resets (low-complexity) may appear more productive than one handling 5 critical system outages (high-complexity). However, the latter’s work has a greater impact on business operations and requires higher skill.

WTCS addresses this gap by:

- Assigning weights to tickets based on complexity, urgency, and business impact.
- Creating a scorecard that reflects the true effort and strategic value of work.
- Encouraging technicians to tackle challenging issues while ensuring fair evaluation.

## Methodology
### 1.) Complexity & Impact Weighting

Tickets are categorized into four tiers based on priority:
- Low = 0.1
- Medium = 0.2
- High = 0.3
- Urgent = 0.4

Add the standard deviation across the last 90 days (calculated separately). We'll denote this as **D** (1.788 in the example).

Optionally, you can apply a small scaling factor (e.g., 0.1) for readability, but the standard implementation multiplies the weighted sum directly by D.
### 2.) WTCS Formula
```
WTCS = Σ(Tickets Resolved × Complexity Weight) × D
```

Example:

Technician A resolves 20 low (×0.1), 10 medium (×0.2), and 1 high (×0.3) ticket:

```
(20 × 0.1) + (10 × 0.2) + (1 × 0.3) = 4.3
4.3 × 1.788 = 7.6884
```

Technician B resolves 30 low (×0.1) and 1 medium (×0.2) ticket:

```
(30 × 0.1) + (1 × 0.2) = 3.2
3.2 × 1.788 = 5.7216
```

Technician A’s score is higher despite resolving fewer tickets, reflecting their focus on high-impact work.

### Automating the Calculation
For a simple command-line example, see [`examples/calculate_wtcs.py`](../examples/calculate_wtcs.py):

```bash
python examples/calculate_wtcs.py --low 20 --medium 10 --high 1 --stddev 1.788
```
This would output `WTCS: 7.6884` for the Technician A scenario above.

## Score Range
Scoring thresholds can be tuned to your environment. The following example ranges assume a standard deviation similar to the example above:

- **1.5+ WTCS/day** – Exemplary performer who consistently resolves complex, high-impact tickets.
- **1.25 WTCS/day** – Strong technician comfortable tackling challenging issues.
- **1 WTCS/day** – Average technician meeting standard expectations.
- **0.25 WTCS/day** – Technician needing additional coaching and support.
