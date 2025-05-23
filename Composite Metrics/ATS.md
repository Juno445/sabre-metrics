# Agent Time Score

## Abstract
Measuring agent efficiency goes beyond just ticket volume. The Agent Time Score (ATS) evaluates how quickly agents respond to and resolve tickets, providing a balanced view of time-based performance metrics that impact customer satisfaction and operational efficiency.

## Introduction
Response and resolution times are critical metrics in IT service management. Customers expect timely acknowledgment and resolution of their issues, making these time-based metrics essential indicators of service quality.

ATS addresses these needs by:
* Combining first response, average response, and resolution times into a single score
* Establishing benchmarks for optimal performance
* Providing a balanced assessment that rewards efficiency without sacrificing quality

## Methodology

### 1.) Time Metrics Weighting
The formula balances three key time metrics with different weightings:
* Resolution Time (50 points maximum) - 70% weight
* Average Response Time (33 points maximum) - 10% weight
* First Response Time (28 points maximum) - 20% weight

### 2.) Bottom 25% Benchmark Adjustment
To account for performance variability and establish realistic benchmarks:
* Calculate the 90-day average for each time metric
* Multiply each average by 0.25 to find the lowest quartile performance benchmark
* Replace the standard maximum values (50, 33, 28) with these calculated benchmarks

This adjustment ensures that scores reflect performance relative to the bottom 25% of historical data, creating a more contextual evaluation.

### 3.) ATS Formula
**ATS = (((50-(AVG((Resolution Time in Bhrs)/3600000)*.7))+(33-(AVG((Avg Response Time in Bhrs)/3600000)*.1))+(28-(AVG((First Response Time in Bhrs)/3600000)*.2))))**

The formula:
- Converts milliseconds to hours (division by 3600000)
- Applies the appropriate weighting factor to each metric (0.7, 0.1, 0.2)
- Subtracts from the maximum possible score for each category

Example:
Agent A has:
- Average Resolution Time: 4 hours (14,400,000 ms)
- Average Response Time: 1 hour (3,600,000 ms)
- Average First Response Time: 30 minutes (1,800,000 ms)

ATS = (((50-(14,400,000/3600000)*.7)+(33-(3,600,000/3600000)*.1))+(28-(1,800,000/3600000)*.2)))
    = (((50-(4*.7))+(33-(1*.1))+(28-(0.5*.2)))
    = (((50-2.8)+(33-0.1)+(28-0.1))
    = ((47.2+32.9)+27.9)
    = 108

## Score Range
* 100+ ATS = Exceptional efficiency, consistently providing rapid responses and resolutions
* 85-99 ATS = Strong performer with good time management skills
* 70-84 ATS = Average performance, meeting basic time expectations
* <70 ATS = Needs improvement in response and resolution times

## Implementation Notes
* Time metrics are measured in business hours (Bhrs) to account for working hours only
* The maximum possible score is 111 (50+33+28) when all response and resolution times are instantaneous
* The bottom 25% benchmark adjustment helps create a more realistic and achievable target
* Negative scores are possible for extremely long handling times and should trigger immediate review
