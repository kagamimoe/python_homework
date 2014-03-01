#

import math

i = [1, 2, 3, 4]
for item in i:
	print item
	print math.sqrt(item)
	if item < 1:
		print 'i < 1'
	elif item >= 1 and item < 2:
		print 'i >= 1'
	else:
		pass

def add(x, y):
	return x + y

print add(1, 2)