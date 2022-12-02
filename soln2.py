MATCHUPS = {
    "A": {
        "X": 3, "Y": 6, "Z": 0
    },
    "B": {
        "X": 0, "Y": 3, "Z":6
    },
    "C": {
        "X":6, "Y": 0, "Z": 3
    }
}
MATCHUPS_2 = {
    "A": {
        "X": 3, "Y": 1, "Z": 2
    },
    "B": {
        "X": 1, "Y": 2, "Z":3
    },
    "C": {
        "X":2, "Y": 3, "Z": 1
    }
}
SHAPE_VALUES = {
    "X": 1, "Y": 2, "Z": 3
}
INPUT_FILENAME = "../../Documents/input.txt"
INPUT = open(INPUT_FILENAME, "r")

score_1 = 0
score_2 = 0
for i in INPUT.readlines():
    score_1 += MATCHUPS[i[0]][i[2]] + SHAPE_VALUES[i[2]]
    score_2 += MATCHUPS_2[i[0]][i[2]] + (SHAPE_VALUES[i[2]]-1)*3 #black magic
print(score_1)
print(score_2)