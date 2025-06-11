import argparse

def calculate_wtcs(low, medium, high, urgent, stddev):
    """Calculate Weighted Ticket Complexity Score."""
    weights = {
        'low': 0.1,
        'medium': 0.2,
        'high': 0.3,
        'urgent': 0.4,
    }
    total = (
        low * weights['low'] +
        medium * weights['medium'] +
        high * weights['high'] +
        urgent * weights['urgent']
    )
    return total * stddev


def main():
    parser = argparse.ArgumentParser(description="Compute Weighted Ticket Complexity Score")
    parser.add_argument('--low', type=int, default=0, help='Number of low complexity tickets')
    parser.add_argument('--medium', type=int, default=0, help='Number of medium complexity tickets')
    parser.add_argument('--high', type=int, default=0, help='Number of high complexity tickets')
    parser.add_argument('--urgent', type=int, default=0, help='Number of urgent complexity tickets')
    parser.add_argument('--stddev', type=float, required=True, help='Standard deviation constant (D)')

    args = parser.parse_args()
    score = calculate_wtcs(args.low, args.medium, args.high, args.urgent, args.stddev)
    print(f"WTCS: {score:.4f}")

if __name__ == '__main__':
    main()
