dp_table_blue = ["b", "l", "u", "e"]
dp_table_clues = ["c", "l", "u", "e", "s"]
dp_table = [
    [0 for _ in range(len(dp_table_blue))] for _ in range(len(dp_table_clues))
]
print(dp_table)

for i in range(len(dp_table_blue)):
    for j in range(len(dp_table_clues)):
        if dp_table_clues[j] == dp_table_blue[i]:
            dp_table[i][j] = dp_table[i-1][i-1] + 1
        else:
            dp_table[i][j] = 0

print(dp_table)
