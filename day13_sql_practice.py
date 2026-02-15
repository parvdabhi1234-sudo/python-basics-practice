import sqlite3

# Connect to SQLite in-memory database

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# 1. Create table

c.execute('''
CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
''')

# 2. Insert data

employees = [
    (1, 'Alice', 'IT', 50000),
    (2, 'Bob', 'HR', 60000),
    (3, 'Charlie', 'IT', 55000),
    (4, 'David', 'Finance', 70000),
    (5, 'Eva', 'HR', 65000)
]

c.executemany('INSERT INTO employees VALUES (?,?,?,?)', employees)
conn.commit()

# 3. Select all

c.execute('SELECT * FROM employees')
print("All Employees:")
for row in c.fetchall():
    print(row)

# 4. Select with WHERE

c.execute('SELECT * FROM employees WHERE department="IT"')
print("\nIT Department Employees:")
for row in c.fetchall():
    print(row)

# 5. Update salary

c.execute('UPDATE employees SET salary = salary * 1.1 WHERE department="HR"')
conn.commit()
c.execute('SELECT * FROM employees WHERE department="HR"')
print("\nUpdated HR Salaries:")
for row in c.fetchall():
    print(row)

# 6. Delete record

c.execute('DELETE FROM employees WHERE id=4')
conn.commit()
c.execute('SELECT * FROM employees')
print("\nAfter Deleting ID 4:")
for row in c.fetchall():
    print(row)

# Close connection

conn.close()

print("\n--- Day 13 SQL Practice Complete ---")
