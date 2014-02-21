reformat = raw_input('Enter some stuff to fix: ')
all_words = []
count_sentence = reformat.count(". ")
start = 0
finish = reformat.find(". ")
for words in range (0,count_sentence+1):
        first_letter = reformat[start]
        if finish > 0:
                rest_word = reformat[start+1:finish]
        else:
                rest_word = reformat[start+1:]
        ind_word = first_letter.upper() + rest_word.lower()
        if finish < 0:
                reformat = reformat
        else:
                reformat = reformat[finish+2:]
                finish = reformat.find(". ")
        all_words.append(ind_word)
        fixed_sentence = ". ".join(all_words)
print fixed_sentence
