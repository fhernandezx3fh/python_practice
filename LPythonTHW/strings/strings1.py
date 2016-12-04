# String Practice

#***************Format Characters***************#
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)
print "x: ", x
print "y: ", y
print

#***************String literal***************#
print "Printing out a string literal."
print

#***************String Formatting***************#
person = {'name': 'Fernando Hernandez', 'age': 34} # Dictionary
#if you don't specify an order, then the first placeholder will be filled by the first format 
sentence1 = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])

#passing in the format arguments in the wrong order
sentence2 = 'My name is {1} and I am {0} years old.'.format(person['name'], person['age'])

#passing the dictionary, specifying keys in placeholders
sentence3 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print "sentence1: ", sentence1
print "sentence2: ", sentence2
print "sentence3: ", sentence3
print

#another example
tag = 'h1'
text = 'This is a headline'
sentence4 = '<{0}>{1}<{0}>'.format(tag, text)
print "sentence4: ", sentence4
print

#using a list instead of dictionary
l = ['Fernando Hernandez', 34]
sentence5 = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
print "sentence5: ", sentence5
print

#***************String Formatting using a Class***************#
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person('Fernando Hernandez', '34')
sentence6 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print "sentence6: ", sentence6
print

#***************String Formatting using kwargs***************#
sentence7 = 'My name is {name} and I am {age} years old.'.format(age='34', name='Fernando Hernandez')
print "sentence7: ", sentence7
print

sentence8 = 'My name is {name} and I am {age} years old.'.format(**person)
print "sentence8: ", sentence8
print

#***************String Formatting numbers***************#
for i in range(1, 11):
  #{:02} pads numbers with zeroes
  sentence9 = 'The value w/o formatting {}. With formatting {:02}'.format(i, i)
  print sentence9
print

pi = 3.14159265
sentence10 = 'Pi is equal to {:.3f}'.format(pi)
print "sentence10: ", sentence10

#***************String Formatting fill and align***************#
print '{:-<30}'.format('left aligned') #fill with dashes
print '{:->30}'.format('right aligned')
print '{:-^30}'.format('center aligned')
print

for align, text in zip('<^>', ['left', 'center', 'right']):
  print zip('<^>', ['left', 'center', 'right'])
  print '{0:{1}{1}16}'.format(text, align)
  print '{0:{fill}{align}16}'.format(text, fill=align, align=align)

''' 
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y) #zip the lists
print zipped
x2, y2 = zip(*zipped) #unzip the list
print x == list(x2) # remember unzipped will produce tuple'''


