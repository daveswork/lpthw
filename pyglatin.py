pyg = 'ay'
original = raw_input('Enter a word.')
word = original.lower()
first = word[0]
vowelword = word+pyg
wordminusfirstletter = word[1:]
newword = wordminusfirstletter+first+pyg

if len(original) > 0 and original.isalpha():
    if first in ["a","e","i","o","u"]:
        print vowelword
    else:
        print newword
else:
    print 'empty'
