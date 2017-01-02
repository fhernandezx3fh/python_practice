from sys import argv
prompt = '> '
print "Enter an additional argument:"
fourth = raw_input(prompt)

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
