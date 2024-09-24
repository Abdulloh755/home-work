import sqlite3

with sqlite3.connect('students.db') as con:
    cursor = con.cursor()
    # cursor.execute('''DROP TABLE IF EXISTS eat''')
    cursor.execute('''CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50),
    last_name  VARCHAR(50),
    hobby TEXT NOT NULL (100),
    birth_yearth INT,
    homework_score INT
    )''')
    cursor.execute('''INSERT INTO students (first_name,last_name,hobby,birth_year,homework_score) VALUES
    ('Ali', 'Nurdinow','football', 2006,8),
    ('Zohridin','Bahridinov','reading',2007,11),
    ('Hamid','Akbarov','Swimming',2007,9)
    ('Abdulloh''Mamirjonov','Basketball',2006,10),
    ('Mamir','Baltabaew','Master',2007,7),
    ('Samardin','Arslonov','Dancing', 2007,3),
    ('Samiy', 'Abduhalilov','Boxing',2008, 9),
    ('Oyaatilla','Usarov','football',2006,8),
    ('Diyor','Abdumominov','Reading',2008,5),
    ('Sadik','MAvlianov','boxing',2007,9)
    ''')

    cursor.execute('''SELECT * FROM student WHERE LENGTH(last_name) > 10''')
    cursor.execute('''UPDATE users SET first_name ='genius'
    WHERE homework_score > 10''')
    cursor.execute('''SELECT * FROM srudent
    WHERE first_name = 'genius' ''');
    cursor.execute('''DELETE FROM student
    WHERE  id % 2 = 0 ''');
    for i in cursor.fetchall():
            print(i)



