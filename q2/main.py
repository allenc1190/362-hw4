# creating an empty list 
lst = [] 

def getN():
	while True:
		try:
			n = int(input("Enter number of elements: "))
			if n > 0:
				break
			raise ValueError()

		except ValueError:
			print("Enter number greater than 0")

	return n

def retList(n):
	for i in range(0, n): 
		ele = int(input("Enter element: ")) 
		lst.append(ele)
	
	print(lst)
	return lst

def average(lst):
	return sum(lst) / len(lst)

def retLen(lst):
	return len(lst)

def retN(n):
	return n

n = getN()
listt = retList(n)
print("The average is:", average(lst))