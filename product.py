#!/usr/bin/env python


from itertools import product


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-delimiter", "--in-delim", default=" ")
    parser.add_argument("-d", "--delimiter", "--delim")
    parser.add_argument(
        "infile",
        nargs="?",
        default="-",
        type=argparse.FileType("r"),
    )
    parsed = parser.parse_args()

    in_delim = parsed.input_delimiter
    # Default the output delimiter to the input delimiter
    delim = parsed.delimiter or in_delim
    infile = parsed.infile

    lists = (
        line.strip().split(in_delim) for line in infile
        if line
    )

    for entry in product(*lists):
        print(delim.join(entry))


if __name__ == "__main__":
    main()

