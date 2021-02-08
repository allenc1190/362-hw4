firstName = input("Enter first name: ")
lastName = input("Enter last name: ")

def fname(firstName):
	return firstName

def lname(lastName):
	return lastName

def retFull(firstName, lastName):
	a = firstName
	b = lastName
	c = a + " " + b
	return c

print(retFull(firstName, lastName))