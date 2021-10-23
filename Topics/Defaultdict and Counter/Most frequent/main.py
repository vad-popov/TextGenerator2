from collections import Counter
text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")
text_list = text.split(" ")
text_counter = Counter(text_list)
freq_counter = text_counter.most_common(int(input()))
print('\n'.join([key+" "+str(value) for key, value in freq_counter]))
