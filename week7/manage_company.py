import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

list_employees = """
SELECT id, name, position
FROM company
"""

monthly = """
SELECT monthly_salary
FROM company
"""

yearly = """
SELECT monthly_salary, yearly_bonus
FROM company
"""

add_employee = """
INSERT INTO company
(name, monthly_salary, yearly_bonus, position)
VALUES(?, ?, ?, ?)
"""

get_name = """
SELECT name
FROM company
WHERE id = {}
"""

delete = """
DELETE FROM company
WHERE id = {}
"""

update = """
UPDATE company SET
name = ?,
monthly_salary = ?,
yearly_bonus = ?,
position = ?
WHERE id = ?
"""


def main():
    while True:
        c = input("command>")

        if c == "list_employees":
            result = cursor.execute(list_employees)
            for line in result:
                print("{} - {} - {}".format(line[0], line[1], line[2]))

        elif c == "monthly_spending":
            result = cursor.execute(monthly)
            spending = sum([salary[0] for salary in result])
            print("The company is spending ${} every month!".format(spending))

        elif c == "yearly_spending":

            result = cursor.execute(yearly)
            spending = sum([salary[0] for salary in result]) * 12

            result = cursor.execute(yearly)
            bonus = sum([salary[1] for salary in result])

            spending += bonus
            print("The company is spending ${} every year!".format(spending))

        elif c == "add_employee":

            empl_name = input("name>")
            empl_salary = input("monthly_salary>")
            empl_bonus = input("yearly_bonus>")
            empl_position = input("position>")

            cursor.execute(add_employee, (empl_name, empl_salary, empl_bonus, empl_position))
            connection.commit()

        elif "delete_employee" in c:
            empl_id = c[16:]
            empl_name = cursor.execute(get_name.format(empl_id))[0]
            cursor.execute(delete.format(empl_id))
            connection.commit()
            print("{} was deleted.".format(name))

        elif "update_employee" in c:

            empl_name = input("name>")
            empl_salary = input("monthly_salary>")
            empl_bonus = input("yearly_bonus>")
            empl_position = input("position>")

            empl_id = c[16:]
            cursor.execute(update, (empl_name, empl_salary, empl_bonus, empl_position, empl_id))
            connection.commit()


if __name__ == '__main__':
    main()
