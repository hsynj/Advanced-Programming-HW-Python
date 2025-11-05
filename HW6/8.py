def extract(s):
    words = s.split()
    result = {}
    idx = 0
    while idx < len(words):
        word = words[idx]
        if word.isalpha() and idx + 1 < len(words) and words[idx + 1].isdigit():
            num = int(words[idx + 1])
            if word not in result:
                result[word] = [num]
            else:
                result[word].append(num)
            idx += 2
        else:
            idx += 1

    final_result = {k: (min(v), max(v)) for k, v in result.items()}
    return final_result

s = "cat dog 3 dog 2 elephant 7 fish 5 elephant 6 fish 15 dog 4 dog 9 elephant 1"
print(extract(s))
