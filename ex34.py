animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
order = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']

def printAnimalAt(number):
	print 'The animal at ' + str(number) + " is the " + str(number + 1) + "st animal and is a " + animals[number] + "."

def printTheAnimal(number):
	print 'The ' + order[number - 1] + "(" + str(number) + "th) animal is at " + str(number - 1) + " and is a" + animals[number - 1] + "." 

printAnimalAt(1)
printTheAnimal(3)
printTheAnimal(1)
printAnimalAt(3)
printTheAnimal(5)
printAnimalAt(2)
printTheAnimal(6)
printAnimalAt(4)