def main():
	sentences = input().split('\n')
	# sentences = "Hello world\nPractice makes perfect".split('\n')
	# 2D list of the input strings, each row consists of the words in each sentence
	newSentences = []
	for sentence in sentences:
		newSentences.append([word.upper() for word in sentence.split(' ')])
	for sentence in newSentences:
		print (' '.join(sentence))

if __name__ == "__main__":
	main()