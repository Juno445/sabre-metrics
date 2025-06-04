# Sabre-Metrics

## Abstract

Traditional IT support metrics often reward superficial volume and speed, missing the deeper business value and real-world impact of support teams. Inspired by advanced sports analytics, this project introduces a data-driven, multi-dimensional framework for measuring, optimizing, and communicating the true value of support teams—including time management, scalability, work complexity, user experience, and direct revenue protection.

---

## Table of Contents

- [Introduction](#introduction)
- [Why Advanced Metrics?](#why-advanced-metrics)
- [Available Metrics](#available-metrics)
- [Business Impact](#business-impact)
- [Implementation](#implementation)
- [Data Requirements](#data-requirements)
- [Sample Usage](#sample-usage)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Just as advanced statistics revolutionized baseball by revealing the hidden value of players, **Sabre-Metrics** was built to move support metrics beyond "tickets resolved" and "average time" into metrics that capture real impact. Our framework equips IT and support leaders with the tools to:

- Benchmark and reward meaningful contributions
- Minimize wasteful support activities
- Tie IT directly to business value

This project is the result of extensive field experience, observation, and analysis, with formulas refined specifically for real-world team environments.

---

## Why Advanced Metrics?

Traditional metrics such as "tickets resolved" or "average resolution time" fail to:

- Account for the varying complexity of tickets (password reset ≠ outage resolution)
- Recognize the risk to business revenue from critical failures
- Prevent agents from avoiding or gaming the system (avoiding tough cases)
- Measure scalability—how well agents maintain efficiency as their workload grows
- Quantify the cost of support to end-user productivity and satisfaction

Our metrics, informed by the lessons of SABRmetrics in sports, shift the focus to a holistic, value-based approach for all stakeholders.

---

## Available Metrics

### Agent Time Score (ATS)
**Measures:** Weighted time management across multiple ticket lifecycle stages to reflect overall efficiency.

### Ticket Complexity Score (TCS)
**Measures:** Weighted completion of tickets by business impact, motivating agents to address higher-value work.

### Real Technician Value (RTV)
**Measures:** An all-in-one metric that synthesizes time efficiency and complexity work, similar to WAR (Wins Above Replacement) in baseball.

### Scalability Performance Score (SPS)
**Measures:** How well an agent maintains efficiency as their assigned workload increases—true "scalability."

### User Friction Score (UFS)
**Measures:** The cumulative time burden and number of touchpoints imposed on users per ticket, surfacing user experience bottlenecks.

### Total Revenue Impact (TRI)
**Measures:** The actual business revenue placed at risk by delayed or failed support, directly connecting support performance to financial outcomes.

Full formulas and methodology for each metric are included in the repository.

---

## Business Impact

By adopting these metrics:
- **Leaders** can see which support agents deliver the highest value—not just the highest output.
- **Teams** gain insights into where process improvements can most benefit users.
- **Executives** receive clear, dollar-quantified evidence of IT’s true business contribution.

Organizations implementing this approach have demonstrated:
- Improved support staff engagement and retention
- Higher end-user satisfaction and productivity
- Reduced revenue-at-risk through proactive management

See our [thesis paper](THESIS.md) in this repo for a deep dive and case study analysis.

---

## Implementation

### Prerequisites

- Data on ticket/resolution times, agent actions, ticket categorization (complexity/priority), endpoints and office locations, and revenue
- Ability to aggregate and process data in SQL, Python, Excel, PowerBI, or similar platforms

### Typical Steps

1. **Data Collection:** Aggregate data from ITSM platforms (e.g., ServiceNow, JIRA, Zendesk)
2. **Metric Calculation:** Apply provided formulas (SQL/Python templates included)
3. **Benchmarking:** Establish baselines and ranges within your organization
4. **Review & Iterate:** Visualize results, gather feedback, adjust weights/thresholds
5. **Report:** Present findings in dashboards and to leadership

---

## Data Requirements

| Metric | Required Fields |
|--------|----------------|
| ATS    | Resolution time, response time, first response time per ticket |
| TCS    | Ticket type/priority and count |
| RTV    | Output of ATS and TCS |
| SPS    | # Tickets per agent, average res time, team averages |
| UFS    | Agent reply count, reassign counts, ticket open time, ticket count |
| TRI    | Ticket impact level, duration, endpoint/office data, revenue |

---

## Sample Usage

See [/examples](examples/) for calculation templates (SQL, Excel, Python) for each metric.

Example—**Agent Time Score (SQL)**:
```sql
SELECT 
  agent_id,
  100 / (
    (AVG(resolution_time_hrs) * 0.5) +
    (AVG(response_time_hrs) * 0.2) +
    (AVG(first_response_time_hrs) * 0.3)
  ) AS agent_time_score
FROM tickets
GROUP BY agent_id;
```
*See the documentation folder for more detailed steps for each metric.*

---

## Contributing

We welcome contributions, discussion, and extension of these metrics! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.  
Areas for collaboration include:
- Industry-specific weighting schemas
- Visualization/dashboard integration
- Additional business-alignment metrics

---

## License

MIT License—see [LICENSE](LICENSE).

---

## Attribution

Please cite this repository, its authors/maintainers, or our [THESIS.md](THESIS.md) in presentations or derivative works.

---

**Questions, feedback, or success stories?**  
Open an issue, pull request, or start a discussion!
