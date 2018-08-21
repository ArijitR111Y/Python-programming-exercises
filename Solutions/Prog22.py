def main():
	word_count = {}
	# string = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.".split(' ')
	string = input().split(' ')
	string.sort()
	for word in string:
		word_count[word] = string.count(word)
	for word in word_count:
		print ("{}:{}".format(word, word_count[word]))


if __name__ == '__main__':
	main()
