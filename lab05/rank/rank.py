#!/usr/bin/env python
import argparse
import sys

__author__ = 'mequrel'


def main():
    parser = argparse.ArgumentParser(description='AGH-GLK PJN Lab05 ranking program.')
    parser.add_argument('-n', '--norm', type=file, help='norm file')

    args = parser.parse_args()
    norm = read_words_from_input(args.norm)
    result = read_words_from_input(sys.stdin)

    ok_count = 0
    for word in norm:
        if not word in result:
            print "{0}: missing in the result".format(word)
        else:
            stemmed_word = norm[word]
            answer = result[word]

            if stemmed_word != answer:
                print "{0}: expected `{1}` but `{2}` was given".format(word, stemmed_word, answer)
            else:
                print "{0}: OK".format(word)
                ok_count += 1

    print "Correctness: {0}/{1}".format(ok_count, len(norm))


def read_words_from_input(input_file):
    """
    Reads file input (word and stemmed word divided by comma) and returns words
    """

    lines = filter(lambda line: line.find(',') > -1, input_file)
    words = map(lambda line: line.strip().split(','), lines)
    return {word: stemmed_word for (word, stemmed_word) in words}


if __name__ == "__main__":
    main()