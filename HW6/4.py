def conv(input_dict):
    result = {}
    for key, values in input_dict.items():
        for value in values:
            if value not in result:
                result[value] = []
            result[value].append(key)
    return result

inp = {'a': [0], 'b': [0], 'c': [0]}
output = conv(inp)
print(output)