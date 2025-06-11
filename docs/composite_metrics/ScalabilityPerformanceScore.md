# Scalability Performance Score (SPS)

## Abstract

"The best agents don't just work fast—they maintain their speed even when the workload increases."  
Traditional IT metrics focus on either speed or volume independently, missing a critical insight: **scalability**. The Scalability Performance Score (SPS) measures an agent's ability to handle increased ticket volume while maintaining efficient resolution times. This metric identifies agents who can take on additional work without compromising quality or speed—essential for workload distribution and capacity planning.

## Introduction

In dynamic IT support environments, workload distribution is often uneven. Some agents naturally gravitate toward higher volumes while others maintain lighter loads. SPS provides a data-driven approach to identify which agents can effectively scale their performance as ticket volume increases.

**Why SPS?**
- Identifies agents capable of handling increased workload without performance degradation
- Provides fair comparison across agents with different ticket volumes
- Enables strategic workload distribution and capacity planning
- Recognizes agents who contribute beyond simple ticket counts

## Methodology

### 1.) Dual-Factor Analysis

SPS evaluates two critical dimensions:
- **Volume Capacity**: How many tickets an agent handles relative to the team
- **Time Efficiency**: How quickly they resolve tickets relative to the team

### 2.) SPS Formula

The formula can be used in two ways:

#### **Individual Assessment (Vacuum Analysis)**
For evaluating an agent's raw performance metrics:
```
Individual_SPS = (Agent_Tickets / Agent_Avg_Resolution_Time)
```
*This gives tickets resolved per unit of time—higher values indicate better throughput.*

#### **Comparative Assessment (Team Benchmarking)**
For comparing an agent's scalability against team performance:
```
Comparative_SPS = (Agent_Tickets / Team_Avg_Tickets) × (Team_Avg_Resolution_Time / Agent_Avg_Resolution_Time)
```

Where:
- `Agent_Tickets` = Total tickets handled by the agent
- `Team_Avg_Tickets` = Average tickets handled per team member
- `Agent_Avg_Resolution_Time` = Agent's average resolution time per ticket
- `Team_Avg_Resolution_Time` = Team's average resolution time per ticket

## Implementation Examples

### Individual SPS Calculation
```sql
-- Individual assessment
SELECT 
    agent_id,
    agent_name,
    ticket_count,
    avg_resolution_hours,
    ROUND(ticket_count / avg_resolution_hours, 2) as individual_sps
FROM agent_metrics;
```

### Comparative SPS Calculation
```sql
-- Team comparison
WITH team_averages AS (
    SELECT 
        AVG(ticket_count) as team_avg_tickets,
        AVG(avg_resolution_hours) as team_avg_resolution
    FROM agent_metrics
)
SELECT 
    a.agent_id,
    a.agent_name,
    a.ticket_count,
    a.avg_resolution_hours,
    ROUND(
        (a.ticket_count / t.team_avg_tickets) * 
        (t.team_avg_resolution / a.avg_resolution_hours), 
        2
    ) as comparative_sps
FROM agent_metrics a
CROSS JOIN team_averages t;
```

## Score Interpretation

### Individual SPS
Higher values indicate better throughput (more tickets per hour of resolution time).

### Comparative SPS
| Score Range | Performance Level | Description |
|-------------|------------------|-------------|
| **2.0+** | 🚀 Elite Scaler | Exceptional volume handling with superior speed |
| **1.5+** | ⭐ High Performer | Above-average volume with above-average speed |
| **1.0** | 📊 Team Baseline | Performs exactly at team average |
| **0.75+** | ⚠️ Developing | Room for improvement in volume or speed |
| **<0.75** | 🎯 Coaching Needed | Requires support to improve scalability |

## Use Cases

### Workload Distribution
- Identify agents capable of handling overflow tickets during peak periods
- Balance workloads based on proven scalability rather than assumptions

### Capacity Planning
- Predict team capacity by understanding individual scaling capabilities
- Plan for growth by identifying agents ready for increased responsibility

### Performance Development
- Coach agents on improving either volume handling or resolution efficiency
- Set realistic performance targets based on scalability metrics

### Team Analysis
- Compare scaling efficiency across different support tiers or specializations
- Identify best practices from high-scaling agents

## Data Requirements

### Required Fields
| Field | Description | Format |
|-------|-------------|---------|
| `agent_id` | Unique agent identifier | String/Integer |
| `ticket_count` | Total tickets handled in period | Integer |
| `avg_resolution_time` | Average time to resolve tickets | Decimal (hours/minutes) |

### Data Quality Considerations
- **Consistent Time Periods**: Ensure all agents are measured over the same timeframe
- **Business Hours**: Use consistent time calculations (business hours vs. calendar time)
- **Ticket Types**: Consider whether to include all ticket types or filter by complexity
- **Minimum Thresholds**: Exclude agents with very low ticket counts for statistical reliability

## Advanced Usage

### Trend Analysis
Track SPS over time to identify:
- Agents improving their scalability
- Seasonal patterns in team scaling efficiency
- Impact of training or process changes

### Segmented Analysis
Calculate SPS for different:
- Ticket priorities (High/Medium/Low)
- Time periods (Peak hours vs. off-hours)
- Ticket categories (Hardware, Software, Network)

## Configuration Examples

### Weighted SPS
For organizations prioritizing speed over volume:
```sql
-- Emphasize resolution time efficiency
Weighted_SPS = (Agent_Tickets / Team_Avg_Tickets)^0.7 × 
               (Team_Avg_Resolution / Agent_Resolution)^1.3
```

## Best Practices

1. **Regular Calibration**: Review team averages monthly to account for process improvements
2. **Context Awareness**: Consider external factors (training periods, system outages, vacation coverage)
3. **Balanced Interpretation**: Use SPS alongside quality metrics (CSAT, first-call resolution)
4. **Transparent Communication**: Share methodology with team members for buy-in and understanding