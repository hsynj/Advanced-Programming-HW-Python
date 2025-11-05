import sqlite3

conn = sqlite3.connect('2.db')
print("-> Opened database successfully")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS TEACHERS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    SUBJECT TEXT NOT NULL
)''')

cursor.execute('''ALTER TABLE STUDENTS
ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
''')

cursor.execute('''INSERT INTO TEACHERS (NAME, SUBJECT) VALUES
('Arian', 'Math'),
('Amirali', 'English'),
('Mohammad', 'Science');
''')

# Update students to assign random teacher IDs between 1-3
cursor.execute('''
UPDATE STUDENTS 
SET teacher_id = CASE
    WHEN ROWID % 3 = 0 THEN 3
    WHEN ROWID % 3 = 1 THEN 1 
    ELSE 2
END;
''')


conn.commit()
conn.close()
