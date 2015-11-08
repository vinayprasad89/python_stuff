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

# Slicing
''' We can access a portion of a list (slice) by specifying the indices of the
slice - from start index to (but not including) the last index '''
numbers = ['zero', 'one', 'two', 'three', 'four', 'five']
first_two_numbers = numbers[0:2]
print first_two_numbers	# prints ['zero', 'one']

# alternate way of getting first 2 elements - start index is assumed to be 0
first_two_elems = numbers[:2]
print first_two_elems	# prints ['zero', 'one']

# similar way to slice from a given index to the end
rest_of_the_list = numbers[2:]
print rest_of_the_list	# prints ['two', 'three', 'four', 'five']

# String slicing - consider a string to be a list of chars
animal = "hippopotamus"
part_of_animal = animal[:5]
print part_of_animal	# prints hippo

# Using index() to find an elem in a list
first_index_of_p = animal.index('p')
print first_index_of_p	# prints 2

animals = ["dog", "cat"]
animals.append(animal)
print animals

# If we index a non-existent element, an exception is raised
# valid index
try:
	print("Index of animal is %d" %animals.index("cat"))
except:
	print "Oops, the animal you're searching for doesn't exist :("
# invalid index
try:
	print(animals.index("dodo"))
except:
	print "Oops, the animal you're searching for doesn't exist :("

# Looping through lists
for animal in animals:
	print(animal.upper())
# Can use for/while loops

# List sorting with sort() and sorted()
sorted_animals = sorted(animals)
print sorted_animals	# prints ['cat', 'dog', 'hippopotamus']

animals.sort()	# sorts the existing list
print sorted_animals	# prints ['cat', 'dog', 'hippopotamus']

# List concatenation
more_animals = ["lion", "fox"]
all_animals = animals + more_animals
print all_animals	# prints ['cat', 'dog', 'hippopotamus', 'lion', 'fox']

# Range() function
print "Range()"

''' It generates a range of numbers and is often paired with the for loop '''
for number in range(3):
	print number  # prints 0, 1, 2

for number in range(2,6):
	print number  # prints 2,3,4,5

print "Odd numbers :"
for odd_num in range(1, 10, 2):
	print odd_num

print "Alternate animals :"
for alt_animal_index in range (0, len(all_animals), 2):
	print all_animals[alt_animal_index]

