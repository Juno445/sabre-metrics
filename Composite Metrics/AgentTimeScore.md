# Agent Time Score (ATS)

## Abstract

“In IT, efficiency isn't about how busy you look—it's about how well you use your time to serve customers.”  
Traditional IT metrics often focus on sheer ticket volume or raw resolution speed, missing the subtleties of effective time management. Agents who communicate promptly, resolve issues quickly, and maintain quality should be recognized for their efficiency—not just the number of tickets they touch. The Agent Time Score (ATS) provides a balanced, weighted measure of an agent's time management to reveal who’s truly excelling in productivity.

## Introduction

In modern IT support environments, agents face pressure to handle tickets swiftly—sometimes at the expense of quality or customer satisfaction. A ticket resolved in half the usual time might indicate proficiency, or it could suggest corners are being cut.  
ATS addresses this by blending resolution time, response time, and first response time into a single, easy-to-compare score. The result is a fair, motivating metric that celebrates agents who consistently strike the right balance between speed and effectiveness.

**Why ATS?**  
- Rewards agents who manage time well
- Promotes consistent, quality service
- Provides a clear comparison to team averages and benchmarks

## Methodology

### 1.) Weighted Averages  
ATS uses three distinct metrics, each with a different impact:
- **Resolution Time** (50% weight) – How long it takes, on average, to fully resolve a ticket.
- **Average Response Time** (20% weight) – How quickly an agent responds to customer replies during a ticket’s lifecycle.
- **First Response Time** (30% weight) – How soon an agent replies to the first customer message.

All time values should be measured in hours.

### 2.) ATS Formula

The basic weighted time calculation is inverted for fairness: **faster times produce higher ATS scores.**
```
ATS = 100 / ((Avg(Resolution Time) * 0.5) + 
             (Avg(Response Time) * 0.2) +
             (Avg(First Response Time) * 0.3))
```
*The constant 100 can be adjusted to best fit your team's environment—calibrate so the "team average" (see below) comes out to roughly 50.*

**Example:**  
Agent A averages:
- **Resolution:** 2 hours
- **Response:** 1 hour
- **First Response:** 0.5 hours

ATS = 100 / ((2*0.5) + (1*0.2) + (0.5*0.3))  
ATS = 100 / (1 + 0.2 + 0.15)  
ATS = 100 / 1.35 = **74.07**

Agent B averages:
- **Resolution:** 4 hours
- **Response:** 2 hours
- **First Response:** 1 hour

ATS = 100 / ((4*0.5) + (2*0.2) + (1*0.3))  
ATS = 100 / (2 + 0.4 + 0.3)  
ATS = 100 / 2.7 = **37.04**

## Score Range

These thresholds are sample values—tweak to match your team’s distribution.
- **100+ ATS / day**: GOAT 🐐  
  Absolutely elite time management. They handle tickets faster than problems can occur, setting the bar for everyone.
- **75+ ATS / day**: All Star ⭐  
  Performs well above average, always responsive and efficient.
- **50 ATS / day**: Team Average 📊  
  Dependable and steady, meeting the expectations for ticket handling and customer service.
- **25 ATS / day**: Below Average ⚠️  
  Time management needs improvement. May benefit from coaching or workflow adjustments.
- **15 ATS / day or less**: Encouragement Needed 🎯  
  Check in to offer support—there’s a real opportunity to help this agent build better habits.

## Notes & Best Practices

- **Sample Size**: Calculate ATS over at least 10 tickets or over a full week/month for trend accuracy.
- **Data Quality**: Ensure resolution and response times ignore tickets paused or waiting for customer input.
- **Customization**: Adjust the weights to reflect organizational priorities (e.g., heavier focus on resolution for highly technical teams).
