from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

''' This can all be condensed into one line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

# We can either use a variable to store the line
all_lines = "%s\n%s\n%s\n"%(line1, line2, line3)

# Or enter it directly as an arg to the write function
target.write("%s\n%s\n%s\n"%(line1, line2, line3))

print "And finally, we can close it."
target.close()
