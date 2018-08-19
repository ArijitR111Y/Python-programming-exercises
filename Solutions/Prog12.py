def check_even(n):
	while n:
		if (n % 10) % 2:
			return False
		n = int(n/10)
	return True

def main():
	num_2 = []
	for number in range(1000, 3001):
		if check_even(number):
			num_2.append(str(number))
	print (', '.join(num_2))

if __name__ == '__main__':
	main()