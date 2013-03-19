#!/usr/bin/env python
import sys
from optparse import OptionParser

MAX_PROPOSITONS = 5
POSITON_WEIGHT = 60
LEN_WEIGHT = 40


def typo_weight(propositions, correct_form):
    """
    Returns real number within [0..1] which is a weight (1-best, 0-worst) of
    how good is a list of propositions.

    1 == there is one proposition which is correct
    0 == correct form is not on proposition list

    :type correct_form: unicode
    :type propositions: list
    :returns: float
    """

    if len(propositions) > MAX_PROPOSITONS:
        return 0.0

    try:
        correct_position = propositions.index(correct_form)
    except ValueError:
        return 0.0

    POSITON_FACTOR = 1.0 * correct_position / (MAX_PROPOSITONS - 1)
    LEN_FACTOR = 1.0 * (len(propositions)-1) / (MAX_PROPOSITONS - 1)

    return 1.0 - 1.0 * (POSITON_WEIGHT * POSITON_FACTOR + LEN_WEIGHT * LEN_FACTOR) / (POSITON_WEIGHT + LEN_WEIGHT)


if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="file with correct forms", metavar="FILE")
    parser.add_option("-v", "--verbose", dest="verbose", help="verbose", action="store_true")

    (options, args) = parser.parse_args()

    with open(options.filename) as correct_file:
        num = 0
        points_total = 0
        for answer in sys.stdin:
            num += 1
            correct = correct_file.readline().strip()
            answer = [word.strip().decode('utf-8') for word in answer.split(',') if word.strip()]
            points = typo_weight(answer, correct)
            if options.verbose:
                print u"Line %d (%s) %s | %.2f points" % (num,  correct, ','.join(answer), points)
            points_total += points

    if options.verbose:
        print u"Total points %.2f of %.2f (max)" % (points_total, num)
    else:
        print u"%.2f" % points_total


