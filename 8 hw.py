import sqlite3

conn = sqlite3.connect('person.db')
cursor = sqlite3.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Departments (DepartmentID)
)
''')

departaments_data=[
    (101,'HR'),
    (102,'IT'),
    (103,'Sales')
]


cursor.executemany('''INSERT INTO Employees (FirstName, LastName, DepartmentID) VALUES (?, ?, ?)', employees_data''')

conn.commit()

cursor.execute('''
SELECT Employees.FirstName,Employees.LastName,
Deparments.DeparmentName
FROM Eployees 
JOIN Deparments ON Eployees.DeparmenID = Departments.DepartmentID
''')

all_employees = cursor.fetchall()

print("Список всех сотрудников с указанием их отделов:")
for employee in all_employees:
    print(f"{employee[0]} {employee[1]} — {employee[2]}")

cursor.execute('''
SELECT Eployees.FirstName, Eployees.LastName
FROM Employees 
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = 'IT'
''')
it_employees = cursor.fetchall()

print("\nСписок сотрудников которые работают в отделе 'IT':")
for employee in it_employees:
    print(f"{employee[0]} {employee[1]}")

conn.close()

