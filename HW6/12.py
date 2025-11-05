entry = [
        {'name': 'Alice', 'age': 25, 'skills': ['Python', 'SQL']},
        {'name': 'Bob', 'age': 35, 'skills': ['Java', 'C++']},
        {'name': 'Charli', 'age': 28, 'skills': ['Python', 'SQL', 'Java']},
        {'name': 'Charlie', 'age': 25, 'skills': ['c++', 'SQL', 'Java']}
]

for index in entry:
    if 20 <= index['age'] <= 30 and {'Python', 'SQL'}.issubset(index['skills']):
        print(index)