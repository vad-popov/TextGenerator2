from nltk import WhitespaceTokenizer
from collections import Counter
from collections import defaultdict
import random
import string

# import re
# Create tokenizer object
tk = WhitespaceTokenizer()

# Get a file name from our user
filename = input()


with open(filename, "r", encoding='utf-8') as corpus_file:
    corpus = tk.tokenize(corpus_file.read())
    #    print("Corpus statistics:")
    #    print("All tokens:", len(corpus))
    #    print("Unique tokens:", len(set(corpus)))
    # bigrams = [(corpus[i], corpus[i + 1]) for i in range(len(corpus) - 1)]
    trigrams = [((corpus[i] + ' ' + corpus[i + 1]), corpus[i + 2])  for i in range(len(corpus) - 2)]
    #    print("Number of bigrams:", len(bigrams))

    trigam_dict = {}

    # {head1: {tail1:2, tail2:3, ...}}
    for i in trigrams:
        trigam_dict.setdefault(i[0], defaultdict(int))
        trigam_dict[i[0]][i[1]] += 1

    # outer loop for sentences
    random.seed()
    for _ in range(10):
        sentence = []

        #find word starting from capital letter
        while True:
            # word = random.choice(corpus[:-1])
            words = random.choice(list(trigam_dict.keys()))
            word_0, word_1 = words.split(" ")
            if word_0[0] in string.ascii_uppercase and word_0[-1] not in '.!?':
                break
        sentence.append(word_0)
        sentence.append(word_1)
        # inner loop for words to add till 5 mandatory words
        for _ in range(3):
            word_2 = Counter(trigam_dict[' '.join((sentence[-2], sentence[-1]))]).most_common(1)[0][0]
            sentence.append(word_2)
        # continue to find a word ending with sentence punctuation
        while sentence[-1][-1] not in '.!?':
            word_2 = Counter(trigam_dict[' '.join((sentence[-2], sentence[-1]))]).most_common(1)[0][0]
            sentence.append(word_2)

        print(' '.join(sentence))
