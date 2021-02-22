#!/usr/bin/env python3

from util import print_week
import argparse


def parse_args() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w',
        '--week',
        help='which week to print (valid values: 1, 2, 3)',
        type=int,
    )
    args = parser.parse_args()
    return args.week


if __name__ == "__main__":
    week = parse_args()
    print_week(week)
