import sqlite3
import sys
from create_company import CreateCompany


class CompanyManager:

    def __init__(self):
        self.db = sqlite3.connect("employees.db")
        self.cursor = self.db.cursor()
        # self.db.row_factory = sqlite3.Row

    def print_list_employees(self):
        self.cursor.execute('''SELECT id, name, position
                                FROM company''')
        # self.db.row_factory = sqlite3.Row
        for row in self.cursor:
            print('{} - {} - {}'.format(row[0], row[1], row[2]))

        self.db.commit()

    def monthly_spending(self):
        self.cursor.execute('''SELECT SUM(monthly_salary)
                                FROM company''')
        for row in self.cursor:
            print('The company is spending ${} every month!'.format(row[0]))
        self.db.commit()

    def yearly_spending(self):
        self.cursor.execute('''SELECT SUM(monthly_salary), SUM(yearly_bonus)
                                FROM company''')
        salaries = self.cursor.fetchall()[0]
        salaries = salaries[0] * 12 + salaries[1]
        print("The company is spending ${} every year!".format(salaries))
        self.db.commit()

    def add_employee(self):
        # id = input("id = ")
        name = input("name: ")
        monthly_salary = input("monthly_salary: ")
        yearly_bonus = input("yearly_bonus: ")
        position = input("position: ")
        self.cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
                                VALUES(?, ?, ?, ?)''', (name, monthly_salary, yearly_bonus, position))
        self.db.commit()

    def delete_employee(self):
        employee_id = input("id: ")
        self.cursor.execute("""DELETE FROM company WHERE id = ?""", employee_id)
        self.db.commit()

    def update_employee(self):
        employee_id = input("id: ")
        name = input("name: ")
        monthly_salary = input("monthly_salary: ")
        yearly_bonus = input("yearly_bonus: ")
        position = input("position: ")
        self.cursor.execute("""UPDATE company
                                SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
                                WHERE id = ?""", (name, monthly_salary, yearly_bonus, position, employee_id))
        self.db.commit()

    def get_command(d, command):
        # command = input("command: ")

        if command == "list_employees":
            CompanyManager.print_list_employees(d)
        elif command == "monthly_spending":
            CompanyManager.monthly_spending(d)
        elif command == "yearly_spending":
            CompanyManager.yearly_spending(d)
        elif command == "add_employee":
            CompanyManager.add_employee(d)
        elif command == "delete_employee":
            CompanyManager.delete_employee(d)
        elif command == "update_employee":
            CompanyManager.update_employee(d)
        elif command == "7":
            sys.exit()
        else:
            print ("Invalid command!")


def main():
    d = CreateCompany()

    print ("Menu:")
    print ("1. list_employees")
    print ("2. monthly_spending")
    print ("3. yearly_spending")
    print ("4. add_employee")
    print ("5. delete_employee ")
    print ("6. update_employee ")
    print ("7. Exit.")

    while True:
        command = input("command: ")
        CompanyManager.get_command(d, command)


if __name__ == '__main__':
    main()
