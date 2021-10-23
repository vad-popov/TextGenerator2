import re

# your code here
word = input()
print(bool(re.match(".+\-.+", word)))