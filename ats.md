# Agent Time Score
## Abstract
By measuring how efficient our team is at managing their time, we can see who is a self starter/self manager, and who may need some additional guidance or direction. 
## Introduction
End user communication is vital to a healthy support desk. If the agents aren't engaging with the users then the users feel a disconnect with IT. When the end users don't feel engaged, that's when escalations happen. An agent's time can be measured on an efficiency scale combining several factors such as avg time to resolove, avg response time, and avg first response time.

ATS addresses this gap by:

* Measuring all time based metrics for efficiency
* Efficiency Metric
* AVG Resolution time, avg

## Methodology
### 1.) Complexty & Impact Weighting
Tickets are categorized into 4 tiers based on priority
* Low = .1
* Medium = .2
* High = .3
* Urgent = .4

Then we add our standard deviation across the last 90 days(calculated separately). Let's assume 1.788 or D

And lastly a *.1 just to make the numbers more readable
### 2.) WTCS Formula
**WTCS=∑(Tickets Resolved×Complexity Weight) x D) x .1**

Example:

Technician A resolves 20 low (.1x), 10 medium (.2x), and 1 high (.3x) tickets:

WTCS=(20×.1)+(10×.2)+(1x.3)=2+2+.3 = 4.3 x 1.788 = **7.6884** 

Technician B resolves 30 low (.1x) and 1 medium (.2x) tickets:

WTCS=(30×.1)+(1×.2)=3+.2= 3.2 x 1.788 = **5.7216**

Technician A’s score is higher despite resolving fewer tickets, reflecting their focus on high-impact work.

## Score Range
This is where things really start to get weird. Obviously your mileage may vary, but the idea is to verify the data matches the observation and this was based on our internal team.
* 1.5+ WTCS/day  = This is a god amonst men. Fear them as they aren't afraid of any ticket. Not only are they not afraid, they'll solve it before you can even release that email.
* 1.25 WTCS/day = Strong Technician, not afraid of a challenge
* 1 WTCS/day = Average run of the mill tech. Nothing special
* .25 WTCS/day = Encouragement needed. Coach this tech and nurture them so they can blossom.
