import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

create_company_table = """
CREATE TABLE IF NOT EXISTS company
(id INTEGER PRIMARY KEY, name TEXT, monthly_salary int, yearly_bonus int, position TEXT)
"""

add_employees = """
INSERT INTO company
(name, monthly_salary, yearly_bonus, position)
VALUES("Ivan Ivanov", 5000, 10000, "Software Developer"),
("Rado Rado", 500, 0, "Technical Support Intern"),
("Ivo Ivo", 10000, 100000, "CEO"),
("Petar Petrov", 3000, 1000, "Marketing Manager"),
("Maria Georgieva", 8000, 10000, "COO")
"""

cursor.execute(create_company_table)
cursor.execute(add_employees)
connection.commit()
