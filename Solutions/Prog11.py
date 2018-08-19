def main():
	# numbers = "0100,0011,1010,1001".split(',')
	numbers = input().split(',')
	divisible_num = []
	for number in numbers:
		num = int(number, 2)
		# for i in range(len(number)):
		# 	num += int(number[len(number)-i-1]) * (2**i)
		if not num % 5:
		 	 divisible_num.append(number)
	print (','.join(divisible_num))


if __name__ == '__main__':
	main()