import random

numbers = random.sample(xrange(100), 69)
#numbers = xrange(10)
#numbers = [3,2,1]

def mysort(list):
	n = len(list) - 1



	while n > -1:
		for item in list:
			if item  > list[n]: #& list.index(item) < n:
				a = list.index(item)
				list.insert(n, list.pop(a))
		n -= 1	
        list2 = list
	end = len(list2) - 1
	while n > -1:
		for item in list2:
			if item  > list2[end]: #& list2.index(item) < n:
				a = list2.index(item)
                                list2.insert(end, list2.pop(a))
                n -= 1
	return list2
	
	
print mysort(numbers)
