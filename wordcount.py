from sys import argv

script, input_file = argv

f = open(input_file)
text_file = f.read()

# split by spaces
lines = text_file.splitlines()
words = " ".join(lines)
words = words.split(" ")

# for each word, make it a key in the dictionary and give value 1
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# print all keys and values
for key,value in word_count.items():
    print key,value



f.close()