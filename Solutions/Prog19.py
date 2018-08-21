from operator import itemgetter

def main():
	values = input().split('\n')
	# values = "Tom,19,80\nJohn,20,90\nJony,17,91\nJony,17,93\nJson,21,85".split('\n')
	entries = []
	for value in values:
		entry = value.split(',')
		entries.append((entry[0], int(entry[1]), int(entry[2])))
	print (sorted(entries, key = itemgetter(0, 1, 2)))



if __name__ == '__main__':
	main()