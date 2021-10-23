# read sums.txt
with open("sums.txt") as sums_file:
    for line in sums_file:
        split_list = line.split(" ")
        print(int(split_list[0]) + int(split_list[1].replace('\n', '')))

