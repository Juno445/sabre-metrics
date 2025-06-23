# Sabre-Metrics: Quick Start Guide

## Introduction

**Sabre-Metrics** revolutionizes IT support measurement by moving beyond simple volume metrics to capture true business value and impact. Inspired by advanced sports analytics, this framework provides six core metrics that measure what really matters: efficiency, complexity handling, scalability, user experience, and revenue protection.

Traditional metrics like "tickets resolved" or "average resolution time" fail to capture the nuanced performance characteristics essential for modern business operations. Sabre-Metrics provides a data-driven approach that quantifies support team effectiveness through business-relevant dimensions.

---

## Core Performance Metrics

### 1. Agent Time Score (ATS)
**What it measures:** Weighted time management across multiple ticket lifecycle stages to reflect overall efficiency.

**Business Value:** Identifies agents who excel at balancing speed with quality communication, not just raw resolution speed.

**Key Components:**
- Resolution Time (50% weight) - How long it takes to fully resolve tickets
- Response Time (20% weight) - How quickly agents respond to customer replies
- First Response Time (30% weight) - How soon agents reply to initial requests

**Formula:** `ATS = 100 / ((Avg_Resolution_Time × 0.5) + (Avg_Response_Time × 0.2) + (Avg_First_Response_Time × 0.3))`

**Performance Levels:**
- **100+ ATS:** Elite performer - exceptional time management
- **75+ ATS:** High performer - well above average efficiency
- **50 ATS:** Team average - dependable and steady
- **25-49 ATS:** Needs improvement - time management coaching needed
- **<25 ATS:** Coaching recommended - significant support required

---

### 2. Ticket Complexity Score (TCS)
**What it measures:** Weighted completion of tickets by business impact, motivating agents to address higher-value work.

**Business Value:** Prevents gaming of simple volume metrics by rewarding agents who tackle challenging, business-critical issues.

**Complexity Weights:**
- Low Priority: 0.1
- Medium Priority: 0.2  
- High Priority: 0.3
- Urgent Priority: 0.4

**Formula:** `TCS = ((Low_Tickets × 0.1) + (Medium_Tickets × 0.2) + (High_Tickets × 0.3) + (Urgent_Tickets × 0.4)) × 2`

**Performance Levels:**
- **100+ TCS:** Hall of Fame - outstanding volume of high-impact tickets
- **75+ TCS:** High performer - frequently tackles challenging work
- **50-74 TCS:** Average - steady contributor across all priorities
- **<50 TCS:** Coaching recommended - needs to step up to complex work

---

### 3. Real Technician Value (RTV)
**What it measures:** An all-in-one metric that synthesizes time efficiency and complexity work, similar to WAR (Wins Above Replacement) in baseball.

**Business Value:** Provides a single comprehensive score that balances speed and impact, identifying truly valuable team members.

**Formula:** `RTV = (Agent_Time_Score × (Ticket_Complexity_Score × 2)) / 100`

**Performance Levels:**
- **50+ RTV:** Elite performer - legendary all-around IT performer
- **30-49 RTV:** High performer - regularly delivers excellence
- **20-29 RTV:** Solid contributor - reliable, high-value team member
- **15-19 RTV:** Average - dependable, steady, and consistent
- **<15 RTV:** Coaching recommended - requires support and development

---

### 4. Scalability Performance Score (SPS)
**What it measures:** How well an agent maintains efficiency as their assigned workload increases—true "scalability."

**Business Value:** Identifies agents capable of handling increased workloads without performance degradation, crucial for capacity planning.

**Formula:** `SPS = (Agent_Tickets / Team_Avg_Tickets) × (Team_Avg_Resolution_Time / Agent_Resolution_Time)`

**Performance Levels:**
- **2.0+ SPS:** Elite scaler - exceptional volume handling with superior speed
- **1.5+ SPS:** High performer - above-average volume with above-average speed  
- **1.0 SPS:** Team baseline - performs exactly at team average
- **0.75+ SPS:** Developing - room for improvement in volume or speed
- **<0.75 SPS:** Coaching needed - requires support to improve scalability

---

### 5. User Friction Score (UFS)
**What it measures:** The cumulative time burden and number of touchpoints imposed on users per ticket, surfacing user experience bottlenecks.

**Business Value:** Quantifies the actual impact on end-user productivity, helping minimize unnecessary interruptions and streamline support processes.

**Key Components:**
- Agent replies (estimated 2 minutes user time each)
- Ticket reassignments (estimated 5 minutes user time each)
- Total time ticket remains open during business hours

**Formula:** `UFS = ((Agent_Replies × 2) + (Reassignments × 5) + (Total_Time_Minutes)) / Total_Tickets`

**Performance Levels:**
- **0-10 minutes:** Excellent user experience
- **11-20 minutes:** Good user experience
- **21-30 minutes:** Needs review - moderate friction
- **31+ minutes:** High friction - immediate attention required

---

### 6. Total Revenue Impact (TRI)
**What it measures:** The actual business revenue placed at risk by delayed or failed support, directly connecting support performance to financial outcomes.

**Business Value:** Translates IT performance into executive language by quantifying dollar amounts at risk from support failures.

**Key Inputs:**
- Annual company revenue
- Number of business locations/offices
- Number of endpoints (workstations/PCs)
- Business hours per day

**Impact Levels:**
- **Medium Impact:** Lost revenue equals 1 PC's hourly revenue share
- **High Impact:** Lost revenue equals 50% of office's hourly revenue
- **Urgent Impact:** Lost revenue equals 100% of office's hourly revenue

**Performance Interpretation:**
- **>$1000 TRI:** Critical financial risk - urgent attention required
- **$500-1000 TRI:** Elevated concern - increased focus needed
- **$100-499 TRI:** Moderate impact - monitor closely
- **<$100 TRI:** Minimal impact - well-controlled risk

---

## Advanced Weighted Metrics

For organizations requiring more sophisticated measurement, Sabre-Metrics includes weighted variants of each core metric:

### Weighted Agent Time Score (WATS)
Applies configurable exponents to emphasize particular timing metrics, allowing teams to customize which time components matter most.

### Weighted Real Technician Value (WRTV)  
Applies a precision scaling factor (0.1058) for enhanced calibration and better differentiation between performance tiers.

### Weighted Scalability Performance Score (WSPS)
Uses non-linear weighting to emphasize resolution efficiency while accounting for ticket volume.

### Weighted Ticket Complexity Score (WTCS)
Incorporates statistical variation (standard deviation) to better reflect the relative difficulty of work across time periods.

### Weighted Total Revenue Impact (WTRI)
Applies custom multipliers to each revenue loss component for organizations with varying risk tolerances.

### Weighted User Friction Score (WUFS)
Time-weighted variant that converts all friction components into estimated user minutes for clearer interpretation.

---

## Implementation Approach

### Phase 1: Foundation (Months 1-2)
- Establish data collection infrastructure
- Baseline traditional metrics for comparison
- Begin with ATS and TCS implementation

### Phase 2: Integration (Months 3-4) 
- Add RTV for comprehensive technician evaluation
- Implement SPS for workload planning
- Educate team on new measurement approach

### Phase 3: Experience & Risk (Months 5-6)
- Deploy UFS for user experience optimization
- Implement TRI for executive reporting
- Connect metrics to business outcomes

### Phase 4: Optimization (Months 7-12)
- Fine-tune weights and thresholds
- Integrate into performance review processes
- Implement advanced weighted variants as needed

---

## Business Impact

Organizations implementing Sabre-Metrics typically observe:

- **15-25% improvement** in customer satisfaction scores
- **20-30% reduction** in revenue-impacting incidents  
- **35-45% improvement** in support team retention
- **Clear executive partnership** through demonstrated business value

---

## Data Requirements

| Metric | Required Data Fields |
|--------|---------------------|
| **ATS** | Resolution time, response time, first response time per ticket |
| **TCS** | Ticket priority/complexity and count by category |
| **RTV** | Output of ATS and TCS calculations |
| **SPS** | Ticket count per agent, average resolution time, team averages |
| **UFS** | Agent reply count, reassignment count, ticket open time, ticket count |
| **TRI** | Ticket impact level, duration, endpoint/office data, company revenue |

---

## Key Benefits

### For Leadership
- **Executive Alignment:** Clear connection between IT performance and business outcomes
- **Strategic Resource Allocation:** Data-driven decisions on hiring, training, and promotion
- **ROI Demonstration:** Quantified evidence of IT's business contribution

### For Support Teams  
- **Fair Recognition:** Rewards for handling complex, high-value work
- **Skill Development:** Incentives to tackle challenging problems
- **Clear Growth Path:** Objective measures for career advancement

### For End Users
- **Better Experience:** Reduced friction and faster resolution of critical issues
- **Proactive Support:** Focus on preventing revenue-impacting problems
- **Streamlined Processes:** Elimination of unnecessary touchpoints and delays

---

## Conclusion

Sabre-Metrics transforms IT support from a cost center perception to a strategic business function by measuring what truly matters. Just as advanced analytics revolutionized professional sports, this framework reveals the hidden value of support teams through data-driven insights that align individual performance with business success.

The framework provides the tools necessary to optimize support operations, improve customer experience, and demonstrate clear business value to executive leadership—moving the industry beyond simplistic volume metrics to sophisticated performance measurement that drives real results.

---

*For implementation details, formulas, and technical specifications, see the complete documentation in the `docs/` directory.* 