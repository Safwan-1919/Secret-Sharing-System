
import argparse
import sys
import os

# Add project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.sharing import split_secret, combine_shares

def main():
    parser = argparse.ArgumentParser(description="Secret Sharing System CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    # Parser for the "split" command
    split_parser = subparsers.add_parser("split", help="Split a secret into multiple shares.")
    split_parser.add_argument("secret", type=str, help="The secret string to split.")
    split_parser.add_argument("-n", "--num_shares", type=int, required=True, help="The total number of shares to generate.")
    split_parser.add_argument("-k", "--threshold", type=int, required=True, help="The minimum number of shares required to reconstruct the secret.")

    # Parser for the "combine" command
    combine_parser = subparsers.add_parser("combine", help="Combine shares to recover the secret.")
    combine_parser.add_argument("shares", type=str, nargs='+', help="The shares to be combined.")

    args = parser.parse_args()

    if args.command == "split":
        try:
            shares = split_secret(args.secret, args.num_shares, args.threshold)
            print("Your secret has been split into the following shares:")
            for i, share in enumerate(shares):
                print(f"  Share {i+1}: {share}")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == "combine":
        try:
            secret = combine_shares(args.shares)
            print(f"Recovered secret: {secret}")
        except Exception as e:
            print(f"Error: Could not recover secret. Ensure you have provided enough valid shares. Details: {e}")

if __name__ == "__main__":
    main()
