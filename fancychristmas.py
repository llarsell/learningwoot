import sys

x = int(sys.argv[1])
n = 1
y = int(sys.argv[1]) 

while x > 0:
	if x > 2:
		print " " * x + "*" * n
	else:
		print " " * y + "*"
	x -= 1
	n += 2
