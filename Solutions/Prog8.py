def main():
	words = input().rstrip().split(',')
	# words = "without,hello,bag,world".rstrip().split(',')
	words.sort()
	print(','.join(words))

if __name__ == '__main__':
	main()