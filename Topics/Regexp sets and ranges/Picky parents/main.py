import re

# your code here
name = input()
print("Suitable!" if bool(re.match("[B-N][aeiouAEIOU]", name)) else "")
