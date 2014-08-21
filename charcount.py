import sys

#word = list(str(sys.argv[1]))

word = sys.argv[1] 

counted = dict((eh,word.count(eh)) for eh in word)

for keys,values in counted.items():
	print('{} : {}'.format(keys,values))
