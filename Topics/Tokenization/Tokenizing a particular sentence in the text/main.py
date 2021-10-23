from nltk.tokenize import sent_tokenize, regexp_tokenize
sentence = input()
num = int(input())
print(regexp_tokenize(sent_tokenize(sentence)[num], "[A-z']+"))