import sys
import MeCab

args = sys.argv
if len(args) != 2:
    sys.exit(1)
str = args[1]
tagger = MeCab.Tagger()
print(tagger.parse(str))
