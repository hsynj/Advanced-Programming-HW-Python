import sqlite3

conn = sqlite3.connect('2.db')
print("-> Opened database successfully")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENTS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT NOT NULL,
GRADE INT NOT NULL
)''')

cursor.execute('''
INSERT INTO STUDENTS (NAME, GRADE) VALUES
('Hossein', 17),
('Sara', 16),
('Ali', 15),
('Zahra', 14),
('Reza', 8);
''')

cursor.execute('''SELECT name, GRADE FROM students;''')
rows = cursor.fetchall()
for row in rows:
    if row[1] >= 15:
        print(f"Name: {row[0]}, GRADE: {row[1]}")


def change_grade(name, grade):
    cursor.execute('''UPDATE STUDENTS SET GRADE = ? WHERE NAME = ?;''', (grade, name))

st_name = input("Enter the name of the student: ")
st_grade = int(input("Enter the new grade: "))
change_grade(st_name, st_grade)

conn.commit()

print("-----------------")
cursor.execute('''SELECT name, GRADE FROM students;''')
rows = cursor.fetchall()
for row in rows:
    if row[1] >= 15:
        print(f"Name: {row[0]}, GRADE: {row[1]}")

# remove student with score less than 10
cursor.execute('''DELETE FROM STUDENTS WHERE GRADE < 10;''')

conn.commit()
conn.close()
