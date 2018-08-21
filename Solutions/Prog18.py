import re

def main():
    words = input().split(',')
    # words = "ABd1234@1,a F1#,2w3E*,2We3345".split(',')

    matched_words =[]

    for word in words:
        if len(word) >= 6 and len(word)<=12:
            if re.search("[a-z]", word) and re.search("[A-Z]", word) and re.search("[0-9]", word) and re.search("[$#@]", word):
                matched_words.append(word)
    print (','.join(matched_words))

if __name__ == '__main__':
    main()