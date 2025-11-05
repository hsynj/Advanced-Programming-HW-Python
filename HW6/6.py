def histogram(d):
    for key in sorted(d.keys()):
        value = int(d[key])
        if value > 0:
            stars = '*' * (value // 5)
            print(f"{key}: {stars}")

histogram({'a': 24, 'c': 75, 'b': 12, 'd': 7.5})
