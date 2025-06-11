# Weighted Ticket Complexity Score
## Abstract
"Technicians don't grow unless they're challenged. Some technicians will naturally seek out a challenge, but this prevents others from being given an opportunity to rise up and learn."

Traditional IT performance metrics often fail to account for the complexity and strategic value of work completed. By treating all tickets equally, organizations risk rewarding volume over impact and stifling growth. This document introduces Weighted Ticket Complexity Score (WTCS), a framework that quantifies the difficulty and importance of tasks to fairly evaluate technician performance. Like SABRmetrics in baseball, WTCS shifts the focus from superficial metrics (e.g., "tickets resolved") to nuanced, data-driven insights that reflect true contribution and potential.

## Introduction
Modern IT environments are dynamic and complex. A technician resolving 50 password resets (low-complexity) may appear more productive than one handling 5 critical system outages (high-complexity). However, the latter’s work has a greater impact on business operations and requires higher skill.

WTCS addresses this gap by:

* Assigning weights to tickets based on complexity, urgency, and business impact.
* Creating a scorecard that reflects the true effort and strategic value of work.
* Encouraging technicians to tackle challenging issues while ensuring fair evaluation.

## Methodology
### 1.) Complexity & Impact Weighting
Tickets are categorized into 4 tiers based on priority
* Low = .1
* Medium = .2
* High = .3
* Urgent = .4

Then we add the standard deviation across the last 90 days (calculated separately). Let's assume 1.788 or **D**.

Finally multiply by `0.1` to keep scores easy to read.
### 2.) WTCS Formula
**WTCS=∑(Tickets Resolved×Complexity Weight) x D)**

Example:

Technician A resolves 20 low (.1x), 10 medium (.2x), and 1 high (.3x) tickets:

WTCS=(20×.1)+(10×.2)+(1x.3)=2+2+.3 = 4.3 x 1.788 = **7.6884** 

Technician B resolves 30 low (.1x) and 1 medium (.2x) tickets:

WTCS=(30×.1)+(1×.2)=3+.2= 3.2 x 1.788 = **5.7216**

Technician A’s score is higher despite resolving fewer tickets, reflecting their focus on high-impact work.

### Automating the Calculation
For a simple command-line example, see [`examples/calculate_wtcs.py`](../examples/calculate_wtcs.py):

```bash
python examples/calculate_wtcs.py --low 20 --medium 10 --high 1 --stddev 1.788
```
This would output `WTCS: 7.6884` for the Technician A scenario above.

## Score Range
Scoring thresholds can be tuned to your environment. The following example ranges assume a standard deviation similar to the example above:
* **1.5+ WTCS/day** – Exemplary performer who consistently resolves complex, high-impact tickets.
* **1.25 WTCS/day** – Strong technician comfortable tackling challenging issues.
* **1 WTCS/day** – Average technician meeting standard expectations.
* **0.25 WTCS/day** – Technician needing additional coaching and support.
