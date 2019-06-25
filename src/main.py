# -*- coding: utf-8 -*-

import sys
import MeCab


def get_text_from_args(args):
    if len(args) != 2:
        sys.exit(1)
    return args[1]


def parse_by_mecab(text):
    tagger = MeCab.Tagger()
    return tagger.parse(text)


if __name__ == "__main__":
    text = get_text_from_args(sys.argv)
    parsed_text = parse_by_mecab(text)
    print(parsed_text)
