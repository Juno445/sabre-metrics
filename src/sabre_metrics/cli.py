"""Command line interface for Sabre-Metrics."""

from __future__ import annotations

import argparse

from .agent_time_score import calculate_ats
from .weighted_agent_time_score import calculate_wats
from .ticket_complexity_score import calculate_tcs
from .weighted_ticket_complexity_score import calculate_wtcs
from .real_technician_value import calculate_rtv
from .weighted_real_technician_value import calculate_wrtv
from .scalability_performance_score import calculate_sps
from .weighted_scalability_performance_score import calculate_wsps
from .user_friction_score import calculate_ufs
from .weighted_user_friction_score import calculate_wufs
from .total_revenue_impact import calculate_tri
from .weighted_total_revenue_impact import calculate_wtri


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Compute Sabre-Metrics values"
    )
    sub = parser.add_subparsers(dest="metric")

    ats_p = sub.add_parser("ats")
    ats_p.add_argument("resolution", type=float)
    ats_p.add_argument("response", type=float)
    ats_p.add_argument("first_response", type=float)

    wats_p = sub.add_parser("wats")
    wats_p.add_argument("resolution", type=float, nargs="+")
    wats_p.add_argument("response", type=float, nargs="+")
    wats_p.add_argument("first_response", type=float, nargs="+")

    tcs_p = sub.add_parser("tcs")
    tcs_p.add_argument("low", type=int)
    tcs_p.add_argument("medium", type=int)
    tcs_p.add_argument("high", type=int)
    tcs_p.add_argument("urgent", type=int)

    wtcs_p = sub.add_parser("wtcs")
    wtcs_p.add_argument("low", type=int)
    wtcs_p.add_argument("medium", type=int)
    wtcs_p.add_argument("high", type=int)
    wtcs_p.add_argument("urgent", type=int)
    wtcs_p.add_argument("stddev", type=float)

    rtv_p = sub.add_parser("rtv")
    rtv_p.add_argument("ats", type=float)
    rtv_p.add_argument("tcs", type=float)

    wrtv_p = sub.add_parser("wrtv")
    wrtv_p.add_argument("ats", type=float)
    wrtv_p.add_argument("low", type=int)
    wrtv_p.add_argument("medium", type=int)
    wrtv_p.add_argument("high", type=int)
    wrtv_p.add_argument("urgent", type=int)

    sps_p = sub.add_parser("sps")
    sps_p.add_argument("agent_tickets", type=float)
    sps_p.add_argument("team_avg_tickets", type=float)
    sps_p.add_argument("agent_res_time", type=float)
    sps_p.add_argument("team_res_time", type=float)

    wsps_p = sub.add_parser("wsps")
    wsps_p.add_argument("agent_tickets", type=float)
    wsps_p.add_argument("team_avg_tickets", type=float)
    wsps_p.add_argument("agent_res_time", type=float)
    wsps_p.add_argument("team_res_time", type=float)

    ufs_p = sub.add_parser("ufs")
    ufs_p.add_argument("reply_count", type=int)
    ufs_p.add_argument("reassign_count", type=int)
    ufs_p.add_argument("time_ms", type=float)
    ufs_p.add_argument("tickets", type=int)

    wufs_p = sub.add_parser("wufs")
    wufs_p.add_argument("reply_count", type=int)
    wufs_p.add_argument("reassign_count", type=int)
    wufs_p.add_argument("time_ms", type=float)
    wufs_p.add_argument("tickets", type=int)

    tri_p = sub.add_parser("tri")
    tri_p.add_argument("medium_loss", type=float)
    tri_p.add_argument("high_loss", type=float)
    tri_p.add_argument("urgent_loss", type=float)
    tri_p.add_argument("violations", type=int)

    wtri_p = sub.add_parser("wtri")
    wtri_p.add_argument("medium_loss", type=float)
    wtri_p.add_argument("high_loss", type=float)
    wtri_p.add_argument("urgent_loss", type=float)
    wtri_p.add_argument("violations", type=int)

    args = parser.parse_args(argv)

    if args.metric == "ats":
        value = calculate_ats(
            [args.resolution],
            [args.response],
            [args.first_response],
        )
    elif args.metric == "wats":
        value = calculate_wats(
            args.resolution,
            args.response,
            args.first_response,
        )
    elif args.metric == "tcs":
        value = calculate_tcs(args.low, args.medium, args.high, args.urgent)
    elif args.metric == "wtcs":
        value = calculate_wtcs(
            args.low,
            args.medium,
            args.high,
            args.urgent,
            args.stddev,
        )
    elif args.metric == "rtv":
        value = calculate_rtv(args.ats, args.tcs)
    elif args.metric == "wrtv":
        value = calculate_wrtv(
            args.ats,
            args.low,
            args.medium,
            args.high,
            args.urgent,
        )
    elif args.metric == "sps":
        value = calculate_sps(
            args.agent_tickets,
            args.team_avg_tickets,
            args.agent_res_time,
            args.team_res_time,
        )
    elif args.metric == "wsps":
        value = calculate_wsps(
            args.agent_tickets,
            args.team_avg_tickets,
            args.agent_res_time,
            args.team_res_time,
        )
    elif args.metric == "ufs":
        value = calculate_ufs(
            args.reply_count,
            args.reassign_count,
            args.time_ms,
            args.tickets,
        )
    elif args.metric == "wufs":
        value = calculate_wufs(
            args.reply_count,
            args.reassign_count,
            args.time_ms,
            args.tickets,
        )
    elif args.metric == "tri":
        value = calculate_tri(
            args.medium_loss,
            args.high_loss,
            args.urgent_loss,
            args.violations,
        )
    elif args.metric == "wtri":
        value = calculate_wtri(
            args.medium_loss,
            args.high_loss,
            args.urgent_loss,
            args.violations,
        )
    else:
        parser.print_help()
        return

    print(f"{value:.2f}")


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
