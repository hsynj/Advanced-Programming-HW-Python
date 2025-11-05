def flatten_dict(d, parent_key=''):
    items = []
    for k, v in d.items():
        new_key = parent_key + '.' + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key))
        else:
            items.append((new_key, v))
    return items

nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}, 'f': 4}
result = flatten_dict(nested_dict)
print(result)