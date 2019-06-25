# -*- coding: utf-8 -*-

import sys
import re
import urllib.parse
import urllib.request
import json
import MeCab


def get_text_from_args(args):
    if len(args) != 2:
        sys.exit(1)
    return args[1]


def parse_by_mecab(text):
    tagger = MeCab.Tagger()
    return tagger.parse(text)


def transfer_to_kanji(word):
    url = "http://www.google.com/transliterate?"
    param = {"langpair": "ja-Hira|ja", "text": word}
    param_encoded = urllib.parse.urlencode(param)
    response = urllib.request.urlopen(url + param_encoded)
    response_data = response.read()
    parsed_data = json.loads(response_data)
    fixed_data = json.loads(json.dumps(parsed_data[0], ensure_ascii=False))
    return fixed_data[1][0]


if __name__ == "__main__":
    text = get_text_from_args(sys.argv)
    parsed_text = parse_by_mecab(text)
    parsed_texts = parsed_text.split("\n")
    elements = [re.split("[\\s,]", item) for item in parsed_texts if item]
    print(elements)
    japinese = []
    for element in elements:
        if element[0] == "EOS":
            continue
        if element[1] == "名詞":
            japinese_item = element[0]
        elif element[1] == "助詞" or element[1] == "連体詞":
            continue
        elif re.match("[ぁ-んァ-ヴ]+", element[0]):
            continue
#            japinese_item = transfer_to_kanji(element[0])
        else:
            japinese_item = re.sub("[ぁ-んァ-ヴ]", "", element[0])
        japinese.append(japinese_item)
    print("".join(japinese))
