def main():
	dimensions = input().split(',')
	# dimensions = "3,5".split(',')
	no_rows, no_col = int(dimensions[0]), int(dimensions[1])
	row = [i for i in range(no_col)]
	matrix = []
	for j in range(no_rows):
		matrix.append([i*j for i in row])
	print (matrix)

if __name__ == '__main__':
	main()