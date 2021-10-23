# put your python code here
grades = input()
percent = grades.split().count('A') / len(grades.split())
print(round(percent, 2))