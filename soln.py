NUMELVES = 3 #set this to 1 for part 1
INPUT_FILENAME = "input.txt"
INPUT = open(INPUT_FILENAME, "r")
sums = []

sum = 0
for i in INPUT.readlines():
    if i == '\n':
        sums.append(sum)
        sum = 0
    else:
        sum += int(i[:-1])

sum_maxes = 0
for i in range(NUMELVES):
    current_max = max(sums)
    sum_maxes += current_max
    sums.remove(current_max)

print(sum_maxes)
