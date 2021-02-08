while True:
	try:
		x = float(input("Enter length of cube: "))
		if x > 0:
			break
		raise ValueError()

	except ValueError:
		print("Enter number greater than 0.")

def calcVol(x):
	return x * x * x

print("The volume of cube is:", calcVol(x))