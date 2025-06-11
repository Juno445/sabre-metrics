# Total Revenue Impact (TRI)

## Abstract

**“Is IT Support a cost center, or a revenue protector?”**  
Traditional IT metrics often miss the bigger picture: unresolved support issues directly threaten revenue by stalling business operations. **Total Revenue Impact (TRI)** provides a quantifiable measure, in dollars, of what’s really at stake during support resolution delays and outages—making IT’s business value crystal clear to leadership.

---

## Introduction

Every ticket delayed, escalated, or violating a resolution SLA doesn’t just irritate staff—it can cost the company real revenue.  
TRI shifts the narrative from “ticket counts” and “SLA %” to **estimated dollars at risk due to support shortfalls**. By leveraging revenue, office, and endpoint data, we connect IT performance straight to the financial language of business outcomes.

---

## Business Logic & Calculations

### **Key Inputs**
| Variable | Description                                   | Example Value            |
|----------|-----------------------------------------------|--------------------------|
| A        | Total annual revenue                          | $3,000,000,000           |
| B        | Number of business locations (offices)        | 250                      |
| C        | Number of endpoints (workstations/PCs)        | 7,500                    |
| E        | Defined business hour window (per day)        | 8                        |

---

### **Step 1. Calculate Contextual Revenue Benchmarks**

1. **Revenue Per Office (D):**
   \[
   D = \frac{A}{B}
   \]
   *Example: D = $3,000,000,000 / 250 = $12,000,000 per office*

2. **Revenue Per PC (G):**
   \[
   G = \frac{D}{C}
   \]
   *Example: G = $12,000,000 / 7,500 = $1,600 per PC annually*

3. **Revenue Per Hour Per Office (F):**
   \[
   F = \frac{D}{E \times \text{Business Days Per Year}}
   \]
   For an annualized metric, specify business days (e.g., 260). For immediate outage calculation, divide per business hour.

---

### **Step 2. Define Revenue Impact Weights**

Each ticket SLA violation is categorized by *potential* hourly revenue loss:

- **Medium Impact:**  
  *Lost revenue equals 1 PC’s hourly share*  
  \[
  \text{Medium Revenue Impact} = \frac{G}{\text{Annual Business Hours}} \times \text{Duration (hrs)}
  \]
  (Annual Business Hours = 8 × business days/year, e.g., 2,080)

- **High Impact:**  
  *Lost revenue per hour equals 50% of that office’s total*
  \[
  \text{High Revenue Impact} = F \times 0.5 \times \text{Duration (hrs)}
  \]

- **Urgent Impact:**  
  *Lost revenue per hour equals 100% of that office’s total*
  \[
  \text{Urgent Revenue Impact} = F \times \text{Duration (hrs)}
  \]

---

### **Step 3. Aggregate Revenue At Risk**

Sum the revenue losses for all SLA-violating tickets, by category:
```plaintext
SUM(Medium Revenue Impact) + SUM(High Revenue Impact) + SUM(Urgent Revenue Impact)
```
Divide by the **number of SLA-violating tickets** for an average per violation (or report total as needed):

\[
\text{TRI} = \frac{ \text{Total Revenue Impacted} }{ \text{Total SLA-violated tickets} }
\]

---

## Final Score: **Total Revenue Impact (TRI)**
The TRI score **directly quantifies the average dollars at risk per SLA-violating ticket**, making it a true “business language” KPI for Support performance.

---

## Example

Given:
- **Annual Revenue (A):** $3,000,000,000
- **Offices (B):** 250
- **Endpoints (C):** 7,500
- **Business Hours/Day (E):** 8
- **Business Days/Year:** 260
- **Total SLA Violations:** 180

Suppose across those tickets:
- Medium Impact = $8,000 lost
- High Impact = $40,000 lost
- Urgent Impact = $75,000 lost

\[
\text{TRI} = \frac{8,000 + 40,000 + 75,000}{180} \approx \$683.33\ \text{average revenue at risk per SLA-violated ticket}
\]

---

## Usage & Interpretation

- **High TRI:** Support failures are putting significant revenue at risk; requires urgent attention.
- **Low TRI:** Your team is keeping major business-impacting issues under control.

**Leadership can immediately see**: “Every critical ticket we miss represents, on average, $X in risked revenue.”

### Sample Score Ranges
| TRI (USD) | Risk Level            |
|-----------|----------------------|
| >1000     | Critical financial risk |
| 500–1000  | Elevated concern       |
| 100–499   | Moderate impact        |
| <100      | Minimal impact         |

---

## Implementation Checklist

- Collect ticket data (category, impact, duration above SLA)
- Define and validate revenue, endpoint, and office numbers annually
- Assign ticket impact levels as part of triage/escalation workflows
- Calculate and review TRI at set intervals (e.g., monthly/quarterly)
- Set targets for TRI reduction over time

---

## Data Requirements

| Field                        | Example Source         |
|------------------------------|-----------------------|
| Ticket impact level          | ITSM/Support system   |
| SLA resolution violation flag| ITSM/Support system   |
| Outage/issue duration        | Ticket logs           |
| Office/endpoint assignments  | Asset/CMDB/HR         |
| Revenue numbers              | Finance               |

---

## Best Practices

- Review outliers—what processes or systems are behind your largest TRI contributors?
- Use TRI in executive dashboards—tie IT to “dollars protected,” not just “tickets closed.”
- Calibrate revenue per office/endpoint each year
- Run scenario analysis: “What if we improved SLA compliance by 10%?”

---

## Configuration & Extension

- Change weights to match business criticality as needed (e.g., some sites are more critical)
- For weighted calculations see [Weighted Total Revenue Impact](../weighted_vs_group/WTRI.md)
- Integrate with real-time outage monitoring for instant TRI estimation during incidents
- Tie TRI to incentive programs for continuous improvement

---

## License

This project is licensed under the GNU General Public License v3.0—see
[LICENSE](../LICENSE) for details.
