#!/usr/bin/env python


import json
import yaml


def main():
    """Entry point."""
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile",
        type=argparse.FileType("r"),
        nargs="?",
        default="-",
    )
    parsed = parser.parse_args()
    print(json.dumps(yaml.safe_load(parsed.infile)))


if __name__ == "__main__":
    main()
