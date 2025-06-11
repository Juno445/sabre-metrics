# Weighted User Friction Score (WUFS)

A time-weighted variant of the standard User Friction Score. Replies and
reassignments are converted into estimated minutes and combined with the total
time a ticket remains open.

## Formula

```
WUFS = (Reply_Count * 2 + Reassign_Count * 5 + Time_Open_ms / 60000) /
       Ticket_Count
```

The score represents the average user minutes lost per ticket.
