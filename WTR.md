# Weighted Ticket Resolution
## Abstract
"Technicians don't grow unless they're challenged. Some technicians will naturally seek out a challenge, but this prevents others from being given an opportunity to rise up and learn."

Traditional IT performance metrics often fail to account for the complexity and strategic value of work completed. By treating all tickets equally, organizations risk rewarding volume over impact and stifling growth. This document introduces Weighted Ticket Resolution (WTR), a framework that quantifies the difficulty and importance of tasks to fairly evaluate technician performance. Like SABRmetrics in baseball, WTR shifts the focus from superficial metrics (e.g., "tickets resolved") to nuanced, data-driven insights that reflect true contribution and potential.

## Introduction
Modern IT environments are dynamic and complex. A technician resolving 50 password resets (low-complexity) may appear more productive than one handling 5 critical system outages (high-complexity). However, the latter’s work has a greater impact on business operations and requires higher skill.

WTR addresses this gap by:

* Assigning weights to tickets based on complexity, urgency, and business impact.
* Creating a scorecard that reflects the true effort and strategic value of work.
* Encouraging technicians to tackle challenging issues while ensuring fair evaluation.

## Methodology
### 1.) Complexty & Impact Weighting
Tickets are categorized into 4 tiers based on priority
* Low = .1
* Medium = .2
* High = .3
* Urgent = .4
### 2.) WTR Formula
**WTR=∑(Tickets Resolved×Complexity Weight)**

Example:

Technician A resolves 20 low (.1x), 10 medium (.2x), and 1 high (.3x) tickets:

WTR=(20×.1)+(10×.2)+(1x.3)=2+2+.3 = *4.3*

Technician B resolves 30 low (.1x) and 1 medium (.2x) tickets:

WTR=(30×.1)+(1×.2)=3+.2= *3.2*

Technician A’s score is higher despite resolving fewer tickets, reflecting their focus on high-impact work.

## Score Range
This is where things really start to get weird. Obviously your mileage may vary, but the idea is to verify the data matches the observation. 
* 1.5+ WTR/day  = This is a god amonst men. Fear them as they aren't afraid of any ticket. Not only are they not afraid, they'll solve it before you can even release that email.
* 1.25 WTR/day = Strong Technician, not afraid of a challenge
* .85 WTR/day = Average run of the mill tech. Nothing special
* .25 WTR/day = Encouragement needed. Coach this tech and nurture them so they can blossom.
