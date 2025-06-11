# User Friction Score (UFS)

## Abstract

"Every touchpoint with IT is either a stepping stone—or a stumbling block—for the user."  
Many IT metrics focus on how efficiently incidents are resolved, but few capture the actual impact on the end user’s time and experience. **User Friction Score (UFS)** measures how much of the user’s time is occupied by agent activity and ticket processes. This metric helps organizations minimize unnecessary user interruptions and streamline support processes for a better overall experience.

---

## Introduction

When a user interacts with IT, support’s job isn’t just to solve the problem—it’s to do so with minimal disruption.  
The User Friction Score is designed to quantify “friction” by capturing the cumulative cost to the user, as measured by:

- The number of direct agent interactions (replies and ticket reassignments), and
- The total time a user’s request remains open during support business hours.

**Why measure UFS?**
- Pinpoint where users face excessive “back-and-forth” or waiting
- Identify opportunities to automate or streamline support
- Benchmark and improve the end-user experience

---

## Formula & Methodology

### **Standard UFS Calculation**

\[
\text{User Friction Score (UFS)} = \frac{
\text{SUM(Agent Reply Count)} + \text{SUM(Agent Reassign Count)} + \left(\frac{\text{SUM(Overall time spent in business hours [ms])}}{3,600,000}\right)
}
{\text{TOTAL(Received Tickets)}}
\]

- *Agent Reply Count*: Total number of agent replies on tickets
- *Agent Reassign Count*: Total handoffs/ticket reassignments among agents
- *Overall time spent in business hours*: The cumulative “clock time” tickets remain open (in ms)
- *Received Tickets*: Tickets received/resolved in the period

**Result:**  
The average “friction score” per ticket.

---

### **Recommended: Time-Weighted UFS (Minutes-Based)**

Because replies and reassigns are counts but time is in hours, the recommended model assigns an estimated user time to each:

- Each *agent reply* is estimated to take ~2 minutes of user attention  
- Each *agent reassign* is estimated at ~5 minutes (extra decision/interruption)  
- Overall time spent is measured in minutes (1 minute = 60,000 ms)

**Formula:**
\[
\text{UFS}_{\text{minutes}} = \frac{
  \left[\text{SUM(Agent Reply Count)} \times 2\right] 
  + \left[\text{SUM(Agent Reassign Count)} \times 5\right] 
  + \left(\frac{\text{SUM(Overall time spent in ms)}}{60,000}\right)
}{
  \text{TOTAL(Received Tickets)}
}
\]

**This gives a clear value: "average user minutes lost per ticket."**

---

## Interpretation

- **Higher UFS = More user friction**  
    (More time, more replies & reassignments—poorer experience)
- **Lower UFS = Smoother user experience**  
    (Fewer interruptions, faster resolutions)

**Example:**  
A UFS_minutes of 22 means, on average, a user spends 22 minutes actively engaged (or waiting) per ticket submitted.

---

## Usage

### Data Requirements

- **Agent reply count** per ticket
- **Agent reassign count** per ticket
- **Total time ticket is open during business hours** (in ms)
- **Received ticket count** for the period

### Basic SQL Example
```sql
SELECT 
  (SUM(agent_reply_count) * 2 
   + SUM(agent_reassign_count) * 5 
   + SUM(overall_time_business_ms) / 60000
  )
  / COUNT(received_ticket_id) AS user_friction_score_minutes
FROM tickets
WHERE ticket_created BETWEEN '2024-01-01' AND '2024-03-31';
```

---

### Benchmarks (Sample Ranges—adjust for your environment)
| UFS (minutes) | User Experience      |
|---------------|---------------------|
| 0–10          | 🌟 Excellent         |
| 11–20         | 👍 Good              |
| 21–30         | ⚠️ Needs review      |
| 31+           | 🚩 High friction     |

---

## Best Practices & Tips

- **Review high-UFS tickets** to find process bottlenecks or unnecessary steps
- **Automate or template common responses/reassignments** to reduce friction
- **Track UFS monthly/quarterly** and set improvement targets
- **Use alongside satisfaction survey data** for a holistic view

---

## Customization & Extension

- Adjust reply and reassign time estimates based on your environment or user feedback
- Weight particularly complex or critical issues with a factor if desired
- Integrate with dashboards for real-time monitoring
