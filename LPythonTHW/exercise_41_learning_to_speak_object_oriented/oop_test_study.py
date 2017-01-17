import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
NUM = []

print WORDS

for number in range(0,10):
  NUM.append(number)


for word in urlopen(WORD_URL).readlines():
    WORDS.append(word)
    WORDS.append(word.strip())

print NUM
print WORDS