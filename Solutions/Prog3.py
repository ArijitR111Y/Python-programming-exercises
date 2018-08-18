def squaresof(n):
	square_dict = {}
	for i in range(n):
		square_dict[i + 1] = (i + 1) * (i + 1)
	return square_dict

def main():
	# n = int(input())
	n = 8
	print (squaresof(n))


if __name__ == "__main__":
	main()