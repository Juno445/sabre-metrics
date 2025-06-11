import argparse
from sabre_metrics.weighted_scalability_performance_score import calculate_wsps
from sabre_metrics.weighted_user_friction_score import calculate_wufs


def calculate_ats(resolution, response, first_response):
    """Compute Agent Time Score."""
    return 100 / ((resolution * 0.5) + (response * 0.2) + (first_response * 0.3))


def calculate_tcs(low, medium, high, urgent):
    """Compute Ticket Complexity Score."""
    return ((low * 0.1) + (medium * 0.2) + (high * 0.3) + (urgent * 0.4)) * 2


def calculate_rtv(ats, tcs):
    """Compute Real Technician Value."""
    return (ats * (tcs * 2)) / 100


def calculate_weighted_sps(agent_tickets, team_avg_tickets, agent_res_time, team_res_time):
    """Compute Weighted Scalability Performance Score."""
    return calculate_wsps(agent_tickets, team_avg_tickets, agent_res_time, team_res_time)


def calculate_weighted_ufs(reply_count, reassign_count, time_ms, ticket_count):
    """Compute time-weighted User Friction Score in minutes."""
    return calculate_wufs(reply_count, reassign_count, time_ms, ticket_count)


def calculate_tri(medium_loss, high_loss, urgent_loss, violations):
    """Average revenue at risk per violating ticket."""
    return (medium_loss + high_loss + urgent_loss) / violations


def calculate_wtcs(low, medium, high, urgent, stddev):
    """Weighted Ticket Complexity Score."""
    weighted_total = (
        (low * 0.1)
        + (medium * 0.2)
        + (high * 0.3)
        + (urgent * 0.4)
    )
    return weighted_total * stddev


def calculate_wrtv(ats, low, medium, high, urgent):
    """Weighted Real Technician Value."""
    weighted_total = (low * 0.1) + (medium * 0.2) + (high * 0.3) + (urgent * 0.4)
    return (ats * weighted_total) * 0.1058


def main():
    parser = argparse.ArgumentParser(description="Compute Sabre-Metrics composites")
    subparsers = parser.add_subparsers(dest="metric")

    ats_p = subparsers.add_parser("ats")
    ats_p.add_argument("resolution", type=float)
    ats_p.add_argument("response", type=float)
    ats_p.add_argument("first_response", type=float)

    tcs_p = subparsers.add_parser("tcs")
    tcs_p.add_argument("low", type=int)
    tcs_p.add_argument("medium", type=int)
    tcs_p.add_argument("high", type=int)
    tcs_p.add_argument("urgent", type=int)

    rtv_p = subparsers.add_parser("rtv")
    rtv_p.add_argument("ats", type=float)
    rtv_p.add_argument("tcs", type=float)

    sps_p = subparsers.add_parser("wsps")
    sps_p.add_argument("agent_tickets", type=float)
    sps_p.add_argument("team_avg_tickets", type=float)
    sps_p.add_argument("agent_res_time", type=float)
    sps_p.add_argument("team_res_time", type=float)

    ufs_p = subparsers.add_parser("wufs")
    ufs_p.add_argument("reply_count", type=int)
    ufs_p.add_argument("reassign_count", type=int)
    ufs_p.add_argument("time_ms", type=float)
    ufs_p.add_argument("tickets", type=int)

    tri_p = subparsers.add_parser("tri")
    tri_p.add_argument("medium_loss", type=float)
    tri_p.add_argument("high_loss", type=float)
    tri_p.add_argument("urgent_loss", type=float)
    tri_p.add_argument("violations", type=int)

    wtcs_p = subparsers.add_parser("wtcs")
    wtcs_p.add_argument("low", type=int)
    wtcs_p.add_argument("medium", type=int)
    wtcs_p.add_argument("high", type=int)
    wtcs_p.add_argument("urgent", type=int)
    wtcs_p.add_argument("stddev", type=float)

    wrtv_p = subparsers.add_parser("wrtv")
    wrtv_p.add_argument("ats", type=float)
    wrtv_p.add_argument("low", type=int)
    wrtv_p.add_argument("medium", type=int)
    wrtv_p.add_argument("high", type=int)
    wrtv_p.add_argument("urgent", type=int)

    args = parser.parse_args()

    if args.metric == "ats":
        print(f"ATS: {calculate_ats(args.resolution, args.response, args.first_response):.2f}")
    elif args.metric == "tcs":
        print(f"TCS: {calculate_tcs(args.low, args.medium, args.high, args.urgent):.2f}")
    elif args.metric == "rtv":
        print(f"RTV: {calculate_rtv(args.ats, args.tcs):.2f}")
    elif args.metric == "wsps":
        print(
            f"Weighted SPS: {calculate_weighted_sps(args.agent_tickets, args.team_avg_tickets, args.agent_res_time, args.team_res_time):.2f}"
        )
    elif args.metric == "wufs":
        print(
            f"Weighted UFS: {calculate_weighted_ufs(args.reply_count, args.reassign_count, args.time_ms, args.tickets):.2f}"
        )
    elif args.metric == "tri":
        print(f"TRI: {calculate_tri(args.medium_loss, args.high_loss, args.urgent_loss, args.violations):.2f}")
    elif args.metric == "wtcs":
        print(f"WTCS: {calculate_wtcs(args.low, args.medium, args.high, args.urgent, args.stddev):.2f}")
    elif args.metric == "wrtv":
        print(f"WRTV: {calculate_wrtv(args.ats, args.low, args.medium, args.high, args.urgent):.2f}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
