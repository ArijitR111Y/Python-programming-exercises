def main():
	# string = "hello world! 123"
	string = input()
	no_letters, no_digits = 0, 0
	for char in string:
		if char.isdigit():
			no_digits += 1
		elif char.isalpha():
			no_letters += 1
	print ("LETTERS {}\nDIGITS {}".format(no_letters, no_digits))

if __name__ == '__main__':
	main()