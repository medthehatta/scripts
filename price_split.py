#!/usr/bin/env python


import json
from collections import defaultdict


def compute_prices(lines):
    totals = {
        "total": 0,
        "totals": defaultdict(float),
        "each": defaultdict(list),
    }
    for line in lines:
        (price, peeps) = line.split(" ", 1)
        peep_list = peeps.split()
        price_each = float(price) / len(peep_list)
        for peep in peep_list:
            totals["total"] += price_each
            totals["each"][peep].append(price_each)
            totals["totals"][peep] += price_each
    return totals


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile",
        type=argparse.FileType("r"),
        default="-",
        nargs="?",
    )
    parsed = parser.parse_args()
    print(json.dumps(compute_prices(parsed.infile)))


if __name__ == "__main__":
    main()
