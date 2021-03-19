#!/usr/bin/env python


import xmltodict
import json
import csv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        type=argparse.FileType("r"),
        nargs="?",
        default="-",
    )
    parsed = parser.parse_args()

    print(json.dumps(xmltodict.parse(parsed.file.read())))


if __name__ == "__main__":
    main()
