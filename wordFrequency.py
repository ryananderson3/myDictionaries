def main():

    infile = open('sometext.txt', 'r')
    text = {}

    for line in infile:
        words = line.split()
        for word in words:
            word = word.lower()
            # removes the , or . if the word ends with it
            if word[len(word)-1:] == '.' or word[len(word)-1:] == ',':
                word = word[0:len(word)-1]
            # if the word is in the dictionary, it increases its value by one
            #if not, then it adds the word to the dictionary
            if word in text:
                text[word] += 1
            else:
                text[word] = 1
    for word in text:
        print(word, '-', text[word])

main()
