import collections
sentence_list = input().lower().split(" ")
Counter = collections.Counter(sentence_list)
print(sorted(Counter.keys()))
