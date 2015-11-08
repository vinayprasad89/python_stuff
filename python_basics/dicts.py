# Python dictionary

''' Usage:
	dict_name = {
		key_1 : value_1,
		key_2 : value_2
  }

  empty_dict = {} '''

states = {	
 	"San Jose" : "CA",
 	"Denver" : "CO",	
}

print ("San Jose is in the state of {}".format(states["San Jose"]))

''' Note : in the last line of the dict above, we can have trailing commas, which is
 		 pretty awesome. It remains consistent every time we add new entries and the best
 		 part is the code diff wouldn't show up for a modified line with just an added
 		 comma.'''

print ("Number of states so far = %d" %len(states))

# Adding elems to dicts
states["Seattle"] = "WA"
print ("Number of states so far = %d" %len(states))

# Deleting an entry with del
del states["Denver"]
print ("Number of states so far = %d" %len(states))

print states
# Checking if a KEY exists
city_to_find = 'Seattle'
if city_to_find in states:
	print 'Found {}'.format(city_to_find)
else:
	print 'Unable to find %s' % city_to_find

city_to_find = "Denver"	# which has been deleted
if city_to_find in states:
	print 'Found {}'.format(city_to_find)
else:
	print 'Unable to find %s' % city_to_find

# Checking if a VALUE exists
state_to_find = "CA"
if state_to_find in states.values():
	print 'Found {}'.format(state_to_find)
else:
	print 'Unable to find %s' % state_to_find

states["Chicago"] = "IL"
states['Albany'] = 'NY'

# Looping through dicts
print "Printing all states"
for state in states.values():
	print state

print 'Printing all cities'
for city in states:
	print city

# Looping using both KEY and VALUE
print "Printing cities and states"
for K, V in states.items():
	print "The city {} is in the state of {}".format(K, V)

# Note that the variables used were named K, V. It can be named city, state or anything
# that makes sense

# Values can be anything 
west_coast_cities = {
	"CA" : ["San Jose", "San Francisco", "Sacramento"],
}

print "Some cities in CA are : {}".format(west_coast_cities['CA'])

# Nested dictionaries
students = {
	"Harry Potter" :	{
		"sex" : "male",
		"height" : "6 feet",	# totally made up
	},
	"Hermione Granger" :	{
		"sex" : "female",
		"height" : "5 feet 8 inches",	# totally made up
	},
}

print "Harry's height is = %s" % students["Harry Potter"]['height']
# Note how single and double quotes are interchangeable throughout the examples

print

# Printing values in nested dicts
# Incorrect
print "Attempt 1 - incorrect"
print "Hermione's info - ".format(students["Hermione Granger"])

print 

# Correct - either access the exact match
print "Attempt 2 - correct"
print "Hermione's info - "
for info in students["Hermione Granger"].values():
	print info

print
# update() method - to update one dict with the values of another
more_cities = {
	"PA" : ["Pittsburgh", "Philadelphia", 'Harrisburg']
}
more_cities.update(west_coast_cities)
print more_cities	# prints {'CA': ['San Jose', 'San Francisco', 'Sacramento'], 'PA': ['Pittsburgh', 'Philadelphia', 'Harrisburg']}
