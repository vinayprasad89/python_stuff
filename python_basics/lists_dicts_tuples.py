# Common usage of 3 of the most popular data structures in python

#####################################################
# Lists
nba_teams = ['warriors', 'lakers', 'cavaliers']
print "The 2015 champs are the {}!!".format(nba_teams[0])

# Can access and modify list elems using their index
random_list = ['lol', 'noob']	# list is 'lol, noob'
print random_list
random_list[1] = 'zzz'	# list is 'lol, zzz'
print random_list

# Negative index - we can access items starting at the end of the list by using
# a negative index. -1 is the last, -2 is the second to last, etc
print random_list[-1]	# prints zzz

# Inserting to a list 
# Using append() method - to insert one item to the end of a list
fruits = ['apples']
fruits.append('mangoes')	# list is apples, mangoes
print fruits[-1]	# prints mangoes

# Using extend method - to insert multiple items
fruits.extend(['grapes', 'peaches'])	# list is apples, mangoes, grapes, peaches
print fruits

# To delete a particular item, using del
del fruits[1]
print fruits	# prints ['apples', 'grapes', 'peaches']

# To overwrite at pos
fruits[2] = 'jackfruit'
print fruits	# prints ['apples', 'grapes', 'jackfruit']

# To insert at pos
fruits.insert(0, 'peaches')
print fruits	# prints ['peaches', 'apples', 'grapes', 'jackfruit']

