# RTV - Real Technician Value

## Abstract

"A truly valuable technician brings more than just speed or ticket volume—they bring skill, impact, adaptability, and efficiency."  
Traditional IT performance metrics often evaluate agents in silos (speed, volume, complexity). **RTV (Real Technician Value)** synthesizes these different aspects into a single, comprehensive score—much like “WAR” (Wins Above Replacement) in baseball. With RTV, you can easily compare and recognize the broad impact of each technician, balancing their efficiency and the difficulty of the problems they solve.

## Introduction

Technicians are often measured by one-dimensional statistics: fastest response, most tickets closed, highest complexity solved. While useful, these miss the mark in capturing a tech’s holistic value to the team and business. RTV merges time management (ATS) and ticket complexity (WTCS), rewarding those who not only work quickly but also tackle challenging, high-impact issues.

**Why RTV?**
- Provides a true “all-around” performance score for each technician.
- Combines efficiency (Agent Time Score) with challenge level (Ticket Complexity Score).
- Helps identify not only specialists but also well-rounded, high-impact teammates.

## Methodology

### 1.) Inputs

**Agent Time Score Composite**  
(See: [Agent Time Score](https://github.com/Juno445/sabre-metrics/blob/main/Composite%20Metrics/ATS.md))  
A weighted measurement (typically 0-100+) that evaluates how efficiently an agent handles their tickets.

**Ticket Complexity Score**  
(See: [WTCS](https://github.com/Juno445/sabre-metrics/blob/main/Composite%20Metrics/TCS.md))  
A weighted count reflecting the difficulty and criticality of the tickets an agent resolves.

### 2.) RTV Formula

The composite RTV blends the above metrics, doubling the emphasis on complexity and scaling within common team scoring ranges.

```
RTV = (Agent Time Score Composite × (Ticket Complexity Score × 2)) / 100
```

**Example:**  
Agent A:
- Agent Time Score Composite = 60
- Ticket Complexity Score = 12

RTV = (60 × (12 × 2)) / 100  
RTV = (60 × 24) / 100  
RTV = 1440 / 100 = **14.4**

Agent B:
- Agent Time Score Composite = 80
- Ticket Complexity Score = 22

RTV = (80 × (22 × 2)) / 100  
RTV = (80 × 44) / 100  
RTV = 3520 / 100 = **35.2**

Agent B’s score reflects both their efficiency and their willingness/ability to take on hard problems.

## Score Range

These thresholds can be tailored to your organization, but are designed for easy benchmarking and encouragement:

| RTV Score | Performance Tier        | Description                                        |
|-----------|------------------------|----------------------------------------------------|
| 50+       | GOAT 🐐                | Legendary all-around IT performer                  |
| 30+       | All Star ⭐             | Elite, regularly delivers excellence               |
| 20+       | Solid Tech 🏅           | Reliable, high-value member of the team            |
| 15        | Average 📊              | Dependable technician, steady and consistent       |
| 10 and <  | Encouragement Needed 🎯 | Could use support—coach for growth and development |

## Notes & Best Practices

- **Transparency:** Share the RTV methodology openly with your team so everyone knows how they are measured.
- **Calibration:** If your average is too high/low, tune scaling factors for ATS or WTCS, or adjust the divisor (100).
- **Context:** Use RTV alongside qualitative observations—great techs can have off weeks or take on non-ticket projects.
- **Sample Size:** Ensure both ATS and WTCS are calculated over a meaningful period/ticket count for fairness.

---

Let me know if you’d like any tweaks or to see documentation for your next metric!
