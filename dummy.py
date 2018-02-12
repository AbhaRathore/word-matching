this_line = []
all_words = []
word_arr = []
f = open('demo.txt', 'r')
lines = f.readlines()
for i in lines:
    this_line.append(i.split(" "))

for i in this_line:
    all_words.append(i[0].strip("[\n]"))

print all_words

def word_matching(k, w, all_words):
    for i in all_words:
        if (i != w):
            word_arr.append(i)
        else:
            word_arr.append(i)
            break
    return word_arr[-(k+1):]

print word_matching(3,'booking', all_words)
