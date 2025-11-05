import sqlite3

conn = sqlite3.connect('2.db')
cursor = conn.cursor()

# show student name and teacher name
cursor.execute('''
SELECT students.name as student_name, teachers.name as teacher_name 
FROM students 
JOIN teachers ON students.teacher_id = teachers.id;
''')

rows = cursor.fetchall()
for row in rows:
    print(f"Student: {row[0]}, Teacher: {row[1]}")


# sort students by grade and show 3 students with highest grade
cursor.execute('''
SELECT name, grade
FROM students
ORDER BY grade DESC
LIMIT 3;
''')

top_students = cursor.fetchall()
print("\nTop 3 students:")
for student in top_students:
    print(f"Name: {student[0]}, Grade: {student[1]}")

# get all students grade average
cursor.execute('''
SELECT AVG(grade) as avg_grade
FROM students;
''')

avg_grade = cursor.fetchone()[0]
print(f"\nAverage grade of all students: {avg_grade:.2f}")


conn.close()
