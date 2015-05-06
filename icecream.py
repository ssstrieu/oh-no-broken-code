# I want to print out my favorite ice cream flavors.

all_flavors = ['chocolate', 'mint', 'strawberry', 'caramel', 'pecan',
               'cookie dough', 'vanilla', 'lemon']
my_faves    = ['mint', 'caramel']

def print_list(my_list):
	for item in my_list:
	    if item in my_faves:
		print "I like {}".format(item)

print print_list(all_flavors)
