
#***************************function: print_heading***************************#
def print_heading(head_str):
  '''Print heading with line max = 79, per PEP-08'''
  print '#{:*^77}#'.format(head_str)

print_heading('Count by X')

#********************Sum without highest and lowest number********************#
def sum_array(arr):
  if arr == None or len(arr) < 3:
    return 0
  return sum(arr) - max(arr) - min(arr)

#*******************************Stringy Strings*******************************#
def stringy(size):
  ''' function stringy that takes a size and returns a string of alternating 
  '1s' and '0s'''
  return "10" * (size / 2) + "1" * (size % 2)

#***************************Are You Playing Banjo?****************************#
''' Create a function which answers the question "Are you playing Banjo?". 
If your name starts with the letter "R" or lower case "r", 
you are playing Banjo!'''
def areYouPlayingBanjo(name):
  return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"

#*************************Number of People in the Bus*************************#
def add(x): return x[0] - x[1]
def number(bus_stops):
  return sum(map(add, bus_stops))

# OR
def number(bus_stops):
  return sum([stop[0] - stop[1] for stop in bus_stops])

#***************************Grasshopper - Summation***************************#
'''Write a program that finds the summation of every number between 1 and num. 
The number will always be a positive integer greater than 0.'''
def summation(num):
  return sum(range(1, num+1))

#**************************A Needle in the Haystack***************************#
'''Write a function findNeedle() that takes an array full of junk but 
containing one "needle". After your function finds the needle it should 
return a message (as a string) that says:
"found the needle at position " plus the index it found the needle'''
def find_needle(haystack):
  return "found the needle at position %s" % haystack.index("needle")

#*******************************Return Negative*******************************#
''' In this simple assignment you are given a number and have to make it 
    negative. But maybe the number is already negative?'''
def make_negative(number):
  return -abs(number)

#*****************Convert number to reversed array of digits******************#
'''You have to return the digits of this number within an array in 
reverse order.'''
def digitize(n):
  return [int(c) for c in reversed(str(n))]
# OR
def digitize(n):
    return map(int, str(n)[::-1])

#*******************************Sum of positive*******************************#
'''You get an array of numbers, return the sum of all of the positives ones.'''
def f(x):
  return x if x > 0 else 0
def positive_sum(arr):
  return sum(filter(f, arr))
# OR
def positive_sum(arr):
  return sum(x for x in arr if x > 0)

#*********************************Count by X**********************************#
'''Create a function with two arguments that will return a list of 
length (n) with multiples of (x).'''
def count_by(x, n):
  return range(x, x*n+1, x)


#************************************Tests************************************#
print sum_array([6, 2, 1, 8, 10])
print sum_array([1, 3])

print stringy(5)

print areYouPlayingBanjo("Rikke")
print areYouPlayingBanjo("martin")

print number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])

print summation(1)
print summation(8)

print find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
print find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])

print make_negative(-5)
print make_negative(0)
print make_negative(1)

print digitize(35231)

print positive_sum([1,-2,3,4,5])

print count_by(50, 5)