def encode(message, key):
    num_cols = len(key)
    num_rows = (len(message) + num_cols - 1) // num_cols
    table = [[message[c*(r+1)] for c in range(num_cols)] for r in range(num_rows)]
    print(table)

    sorted_key = sorted(list(key))
    result = ''

    for ch in sorted_key:
        col_index = key.index(ch)
        for r in range(num_rows):
            if table[r][col_index]:
                result += table[r][col_index]

    return result


def decode(encoded_message, key):
    num_cols = len(key)
    num_rows = (len(encoded_message) + num_cols - 1) // num_cols
    table = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    col_lengths = [num_rows] * num_cols
    extra = num_cols * num_rows - len(encoded_message)
    for i in range(extra):
        col_lengths[num_cols - 1 - i] -= 1

    sorted_key = sorted(list(key))

    idx = 0
    for ch in sorted_key:
        col_index = key.index(ch)
        for r in range(col_lengths[col_index]):
            table[r][col_index] = encoded_message[idx]
            idx += 1

    result = ''
    for r in range(num_rows):
        for c in range(num_cols):
            if table[r][c]:
                result += table[r][c]

    return result


message = input("Enter your text for coding or de-coding: ")
key = input("Enter your key: ")

if len(key) < 1:
    print("Key is or higher than 1.")
else:
    mode = input("1. Coding\n2. De-Coding\n>>")

    if mode == '1':
        result = encode(message, key)
        print("Coding text:", result)
    elif mode == '2':
        result = decode(message, key)
        print("De-Coding Text:", result)
    else:
        print("Unknown entry!")
