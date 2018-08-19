def main():
	# numbers = "1,2,3,4,5,6,7,8,9".split(',')
	numbers = input().split(',')
	new_numbers = [int(n)*int(n) for n in numbers if int(n) % 2 ]
	print (new_numbers)

if __name__ == '__main__':
	main()