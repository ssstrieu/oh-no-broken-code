import string
uppers = string.uppercase
username= raw_input('what is your name...')

first_letter= username[0].upper() #returns capitalized the first letter in user's name
first_position= uppers.find(first_letter)
superheroList=[]

with open('names.txt') as f:
	for line in f:
		superheroList.append(line.strip('\n'))

print "Hi "+ username+". Your superheroine name is... "+ superheroList[first_position] 
#part 2


import random

firstnames=[]
lastnames=[]

for name in superheroList:
	firstnames.append(name.split(' ')[0])
	lastnames.append(name.split(' ')[1])

randoName=random.choice(firstnames)+" "+ random.choice(lastnames)

print "Your random superheroine name is: " + randoName














