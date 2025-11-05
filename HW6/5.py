dic1 = {'a': 5, 'b': 'hello', 'c': 3}
dic2 = {'a': 2, 'b': 3, 'd': 4}
conv = {}

for key, itm in dic1.items():
    conv[key] = itm

for key, itm in dic2.items():
    if key in conv:
        if isinstance(conv[key], str):
            conv[key] += str(itm)
        else:
            conv[key] += itm
    else:
        conv[key] = itm


print(conv)