# Strings in python can be represented both by single and double quotes

str1 = 'This works'
str2 = "This works too!"

print str1
print str2
#print str1 + '\n' + str2	#Alt way of printing in same format

# Ways to use quotation marks in the string itself
sentence = 'Vinay said, "Where is my beer?"'
print sentence

# Escape the offending quotation mark
sentence = "Vinay said, \"Where is my beer?\""
print sentence

# Escape single quotation mark similarly
sentence = 'Vinay said, "Enough of beers; where\'s my whiskey at?!"'
print sentence

# Indexes
a = 'apple'[0]
print a
# Alternatively
fruit = "apple"
first_char = fruit[0]
print first_char

# Some string methods
print (len(fruit))

# To upper and lower cases
print (fruit.upper())
print (fruit.lower())

# String concatenation
dessert = "pie"
print fruit + dessert

# Repeating strings
print 'ha' * 10

# str() - to convert to a string
year = 2015
print 'The year is ' + str(year)

# String formatting with placeholders using format()
name = 'Vinay'
language = 'Python'
print "My name is {}, and I'm learning {}".format(name, language)

# User input using input()
name = input("Whats your name? ")
print ('{} is such a weird name o.0'.format(name))
# Note that with input(), the input entered must be enclosed in quotes, or python
# will consider it to be a variable.

# User input using raw_input() - doesn't require the quotes
place = raw_input("Ok, Where do you live? ")
print ("I've heard a lot of scary stuff about {}!!".format(place))



