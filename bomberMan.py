matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

rows = set()
cols = set()

for r, row in enumerate(matrix):
    for c, val in enumerate(row):
        if val:
            rows.add(r)
            cols.add(c)

print((len(matrix) - len(rows)) * (len(matrix[0]) - len(cols)))
