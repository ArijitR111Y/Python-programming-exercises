def main():
	l = []
	for i in range(2000, 3201):
		if not i % 7 and i %  5:
			l.append(str(i))
	print (', '.join(l))

if __name__ == '__main__':
	main()