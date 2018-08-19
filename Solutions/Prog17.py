def main():
	transactions = input().split('\n')
	# transactions = "D 300\nD 300\nW 200\nD 100".split('\n')
	bal = 0
	for transaction in transactions:
		if transaction[0] == 'D':
			bal += int(transaction[2:])
		elif transaction[0] == 'W':
			bal -= int(transaction[2:])
	print (bal)

if __name__ == '__main__':
	main()