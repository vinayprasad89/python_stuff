from collections import namedtuple

# Tuples are essentially immutable lists, closed in ()
# They are used to store groups of related fields

# Simple tuple
two_words = ('hello', 'world')
print two_words
print two_words[-1]

# Immutable - we cannot modify the value once it has been created
#two_words[0] = 'new'	# raises TypeError: 'tuple' object does not support item assignment

# To create a tuple with a single elem, we must have a trailing comma at the end
#example_tuple = (5)
#print example_tuple[0]	# raises TypeError: 'int' object has no attribute '__getitem__'

example_tuple = (1,)
print example_tuple[0]

''' Think of it this way. We want the output of (1 + 2) * 3 to be 9 and not
(3, 3, 3) '''

# Tuples are generally used for data whose values do not change.
days_of_the_week = ('Mon', 'Tue', 'Wed', "Thu", "Fri", 'Sat', 'Sun')
print days_of_the_week	# prints ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print days_of_the_week[5]	# prints Sat

# To create a list from a tuple
days_of_the_week_list = list(days_of_the_week)
print days_of_the_week_list	# prints ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# can modify list elems
days_of_the_week_list[5] = 'Saturday'
print days_of_the_week_list	# prints ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Saturday', 'Sun']

# To create a tuple from a list
days_of_the_week_list_tuple = tuple(days_of_the_week_list)
print days_of_the_week_list_tuple	# prints ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Saturday', 'Sun')

# Tuples as function return types
def high_and_low_scores(scores):
	high = max(scores)
	low = min(scores)
	return (high, low)	# return a tuple

scores = [69, 74, 99, 75]
(high_score, low_score) = high_and_low_scores(scores)
print (high_score, low_score)

# Named tuples - to be able to access by names, and when attributes will not change
# Note - we need to import collections first (done at the beginning of this module)
Employee = namedtuple("Employee", ['id', 'title', 'salary', 'company'])
#e = Employee()	# raises TypeError: __new__() takes exactly 5 arguments (1 given)
employee_1 = Employee(10, 'Chief Clown', 850000, 'RandomCompanyName')
print employee_1  # prints TypeError: __new__() takes exactly 5 arguments (1 given)

# Access attributes using dot notation
print "Company name is %s " % employee_1.company

# Creating namedtuples from an iterable using _make()
new_employee_data = [11, 'Noob Clown', 50, 'RandomCompanyName']
employee_2 = Employee._make(new_employee_data)
print employee_2

