# Ticket Complexity Score (TCS)

## Abstract

"Teams become stronger when individuals rise to the challenge."  
Traditional ticket metrics often count all tickets equally, failing to reward those who resolve the most demanding problems. **Ticket Complexity Score (TCS)** introduces priority-based weights that encourage agents to step into more complex, high-impact work—ensuring that effort and ability are recognized, not just volume.

## Introduction

Not all tickets are created equal. A technician who handles urgent, high-complexity tickets provides greater business value than one who sticks to easy, low-impact issues. TCS recognizes agents who seek out and resolve tougher tickets by assigning a higher value to those critical efforts. This score helps foster excellence, growth, and fair measurement across your support organization.

**Why TCS?**
- Motivates agents to handle more impactful and high-priority tickets
- Clarifies how different types of work contribute to overall performance
- Promotes both skill development and business-critical problem solving

## Methodology

### 1.) Ticket Priority Weighting

Each ticket is assigned a weight according to its priority:

- **Low Priority:** 0.1
- **Medium Priority:** 0.2
- **High Priority:** 0.3
- **Urgent Priority:** 0.4

### 2.) TCS Formula

Multiply the number of tickets in each category by its weight, then sum the results and multiply by 2 for visibility and impact.

```
TCS = ((Low Tickets × 0.1) + (Medium Tickets × 0.2) + (High Tickets × 0.3) + (Urgent Tickets × 0.4)) × 2
```

#### Example

Tech A resolves:
- 15 Low
- 10 Medium
- 5 High
- 2 Urgent

TCS = ((15 × 0.1) + (10 × 0.2) + (5 × 0.3) + (2 × 0.4)) × 2  
TCS = (1.5 + 2 + 1.5 + 0.8) × 2  
TCS = 5.8 × 2 = **11.6**

Tech B resolves:
- 10 Low
- 3 Medium
- 4 High
- 1 Urgent

TCS = ((10 × 0.1) + (3 × 0.2) + (4 × 0.3) + (1 × 0.4)) × 2  
TCS = (1 + 0.6 + 1.2 + 0.4) × 2  
TCS = 3.2 × 2 = **6.4**

## Score Range

| TCS Score | Performance Tier          | Description                                               |
|-----------|--------------------------|-----------------------------------------------------------|
| 100+      | Hall of Famer 🏆          | Handles an outstanding volume of high-weight tickets       |
| 75+       | All Star ⭐               | Frequently takes on challenging or urgent work             |
| 50        | Average 📊                | Steady contributor across all priorities                  |
| 35 and <  | Encouragement Needed 🎯   | Needs to step up to more complex tickets for growth        |

*Note: With these weights, only extremely high-volume agents will break 50+ in a typical period. Adjust multipliers or review your scoring expectations to fit your team's environment.*

## Notes & Best Practices

- **Visibility:** Use the TCS alongside other KPIs—efficiency, customer satisfaction, etc.—for a holistic view.
- **Coaching:** Leverage low TCS scores to identify coaching opportunities for agents hesitant to take on heavier workloads.
- **Customization:** Adjust weights or the final multiplier for your team’s ticket mix and growth priorities.
- **Data Quality:** Review that tickets are correctly prioritized in your system to ensure fair scoring.
