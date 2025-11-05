import sqlite3

conn = sqlite3.connect('1.db')
print("-> Opened database successfully")

cursor = conn.cursor()

cursor.execute('''
SELECT e.name
FROM employees e
JOIN departments d ON e.department_id = d.id
JOIN projects p ON d.id = p.department_id
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
)
AND p.budget > 100000;
''')

rows = cursor.fetchall()
for row in rows:
    print(f"Employee Name: {row[0]}")

cursor.execute('''
DELETE FROM employees WHERE name = 'Sara';
''')
conn.commit()
conn.close()
