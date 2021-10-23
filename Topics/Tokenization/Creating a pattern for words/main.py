from nltk.tokenize import regexp_tokenize
sentence = input()
index = int(input())
print(regexp_tokenize(sentence, "[A-z]+")[index])