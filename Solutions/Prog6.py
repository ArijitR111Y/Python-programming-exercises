def main():
	values = input().split(',')
	# values = "100,150,180".split(',')
	calc_values = []
	for each in values:
		calc_values.append(str(round((int(each)*2*5/3)**0.5)))
	print (','.join(calc_values))

if __name__ == '__main__':
	main()