# A function must be defined before it is used.
def print_hello_world():
	print 'Hello, world!'
print_hello_world()

def print_message(message):
	print message
print_message("YOLO")

def greet_user(user_name):
	print ("Hello, {}!".format(user_name))
greet_user("Vinay")

# We can have default args values
def greet_user_1(user_name="VinayPrasad"):
	print ("Hello, {}!".format(user_name))
greet_user_1()	# prints the default value specified

# We can override default values
def greet_user_2(user_name="VinayPrasad"):
	print ("Hello, {}!".format(user_name))
greet_user_2("R2-D2")	
