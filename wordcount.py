from sys import argv

script, input_file = argv

f = open(input_file)
text_file = f.read().lower()

def normalize(string):
    string = string.lower()
    for i in string:
        if not i.isalpha() and not i.isspace():
            string = string.replace(i, "")
    return string

def sort_by_freq_and_alpha(dict):
    new_dict = {}
    for key,val in dict.iteritems():
        if val not in new_dict:
            new_dict[val] = [key]
        else:
            new_dict[val].append(key)
            new_dict[val].sort()
    return new_dict


words = normalize(text_file).split()

# for each word, make it a key in the dictionary and give value 1
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = sort_by_freq_and_alpha(word_count)

for key,val in sorted_word_count.iteritems():
    print key,val
        

f.close()
