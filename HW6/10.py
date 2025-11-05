l = ['home/user/documents', 'home/user/images', 'home/user/downloads']

result = {}

for words in l:
    parts = words.split('/')
    current = result
    for part in parts:
        current = current.setdefault(part, {})

print(result)
