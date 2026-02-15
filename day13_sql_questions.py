import sqlite3

# Setup same as main code

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE employees(id INTEGER, name TEXT, department TEXT, salary REAL)')
employees = [(1,'Alice','IT',50000),(2,'Bob','HR',60000),(3,'Charlie','IT',55000)]
c.executemany('INSERT INTO employees VALUES (?,?,?,?)', employees)
conn.commit()

# Q1: Select all employees

c.execute('SELECT * FROM employees')
print("Q1:", c.fetchall())

# Q2: Select employees in IT department

c.execute('SELECT * FROM employees WHERE department="IT"')
print("Q2:", c.fetchall())

# Q3: Update salary of Bob to 65000

c.execute('UPDATE employees SET salary=65000 WHERE name="Bob"')
conn.commit()
c.execute('SELECT * FROM employees WHERE name="Bob"')
print("Q3:", c.fetchall())

# Q4: Delete employee with id=1

c.execute('DELETE FROM employees WHERE id=1')
conn.commit()
c.execute('SELECT * FROM employees')
print("Q4:", c.fetchall())

# Q5: Count number of employees

c.execute('SELECT COUNT(*) FROM employees')
print("Q5:", c.fetchone())

conn.close()
