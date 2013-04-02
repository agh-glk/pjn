#!/usr/bin/env python
import argparse
import sys

__author__ = 'cypreess'


def read_sets_from_input(f):
    """
    Reads file input (lines divided into sets by # signs) and returns a sets
    """
    sets = {}
    current = set()
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            # Comment found, splitting sets
            current = set()
        elif line:
            current.add(line)
            sets[line] = current
    return sets

def f1(norm, answer):
    """
    Calculates F1 Score as defined here: http://en.wikipedia.org/wiki/F1_score
    """
    common_positive = norm.intersection(answer)
    precision = float(len(common_positive)) / len(answer)
    recall = float(len(common_positive)) / len(norm)
    return 2.0 * (precision * recall) / (precision + recall)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='AGH-GLK PJN Lab03 ranking program.')
    parser.add_argument('-n', '--norm', type=file, help='norm file')

    args = parser.parse_args()
    norm = read_sets_from_input(args.norm)
    answer = read_sets_from_input(sys.stdin)

    results = []
    for line in answer:
        if not norm.has_key(line):
            results.append(0)
        else:
            results.append(f1(norm[line], answer[line]))

    print reduce(lambda x, y: x + y, results) / len(results)
