def fact(n):
	if n == 1 or n == 0:
		return n
	return n * fact(n-1)

def main():
	# x = int(input())
	x = 8
	print (fact(x))

if __name__ == '__main__':
	main()