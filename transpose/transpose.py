def transpose(input_lines):
    rows = [[] for _ in len(input_lines[0])]
    for r, row in enumerate(input_lines):
        for char in row:
            rows[r].append(char)
    return [''.join(row) for row in rows]
