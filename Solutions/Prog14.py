def main():
	# string = "Hello world!"
	string = input()
	no_upper, no_lower = 0, 0
	for char in string:
		if char.isupper():
			no_upper += 1
		elif char.islower():
			no_lower += 1
	print ("UPPER CASE {}\nLOWER CASE {}".format(no_upper, no_lower))

if __name__ == '__main__':
	main()