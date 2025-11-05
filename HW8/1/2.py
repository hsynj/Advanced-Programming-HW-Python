import sqlite3

conn = sqlite3.connect('1.db')
print("-> Opened database successfully")
cursor = conn.cursor()

# Employees
cursor.execute('''
INSERT INTO employees (id, name, department_id, salary) VALUES
(1, 'Hossein', 1, 120000),
(2, 'Sara', 1, 90000),
(3, 'Ali', 2, 85000),
(4, 'Zahra', 3, 125000),
(5, 'Reza', 3, 90000);
''')
print("-> Employees created successfully")

# Departments
cursor.execute('''
INSERT INTO departments (id, name, location) VALUES
(1, 'Engineering', 'Tehran'),
(2, 'Marketing', 'Shiraz'),
(3, 'HR', 'Tabriz');
''')
print("-> Departments created successfully")

# Projects
cursor.execute('''
INSERT INTO projects (id, name, budget, department_id) VALUES
(1, 'AI System', 150000, 1),
(2, 'Ad Campaign', 80000, 2),
(3, 'Recruitment Drive', 120000, 3),
(4, 'Optimization', 95000, 1);
''')
print("-> Projects created successfully")

print("-> Records created successfully")
conn.commit()
conn.close()
