# Regular import
import ex25
print "First Run"
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
print words
sorted_words = ex25.sort_words(words)
print sorted_words
ex25.print_first_word(words)
ex25.print_last_word(words)
print words
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print sorted_words
sorted_words = ex25.sort_sentence(sentence)
print sorted_words
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)

print "\n\n"

# typing ex25 is annoying so we can import all modules from ex25
from ex25 import *
print "Second Run"
sentence = "All good things come to those who wait."
words = break_words(sentence)
print words
sorted_words = sort_words(words)
print sorted_words
print_first_word(words)
print_last_word(words)
print words
print_first_word(sorted_words)
print_last_word(sorted_words)
print sorted_words
sorted_words = sort_sentence(sentence)
print sorted_words
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)