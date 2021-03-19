#!/usr/bin/env python


import json
import csv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "csv",
        type=argparse.FileType("r"),
        nargs="?",
        default="-",
    )
    parsed = parser.parse_args()

    reader = csv.DictReader(parsed.csv, delimiter=",")
    for record in reader:
        print(json.dumps(record))


if __name__ == "__main__":
    main()
