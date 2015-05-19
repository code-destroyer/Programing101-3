import sqlite3
import sys
from create_company import CreateCompany


class CompanyManager:

    def __init__(self):
        self.db = sqlite3.connect("create_company.db")
        self.cursor = self.db.cursor()

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
            print('The company is spending {} every month!'.format(row[0]))

    def yearly_spending(self):
        self.cursor.execute('''SELECT SUM(monthly_salary), SUM(yearly_bonus)
                                FROM company''')
        salaries = self.cursor.fetchall()[0]
        salaries = salaries[0] * self.months + salaries[1]
        return salaries

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        name = input("name: ")
        monthly_salary = input("monthly_salary: ")
        yearly_bonus = input("yearly_bonus: ")
        position = input("position: ")
        self.cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
                                VALUES(?, ?, ?, ?)''', name, monthly_salary, yearly_bonus, position)
        self.connection.commit()

    def delete_employee(self, employee_id):
        employee_id = input("id: ")
        self.cursor.execute("""DELETE FROM company WHERE id = ?""", employee_id)
        self.connection.commit()

    def update_employee(self, name, monthly_salary, yearly_bonus, position, employee_id):
        employee_id = input("id: ")
        name = input("name: ")
        monthly_salary = input("monthly_salary: ")
        yearly_bonus = input("yearly_bonus: ")
        position = input("position: ")
        self.cursor.execute("""UPDATE company
                                SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
                                WHERE id = ?""", name, monthly_salary, yearly_bonus, position, employee_id)
        self.connection.commit()

    def get_command(database, command):
        command = input("command: ")

        if command == 1:
            CompanyManager.print_list_employees(database)
        elif command == 2:
            CompanyManager.monthly_spending(database)
        elif command == 3:
            CompanyManager.yearly_spending(database)
        elif command == 4:
            CompanyManager.add_employee(database)
        elif command == 5:
            CompanyManager.delete_employee(database)
        elif command == 6:
            CompanyManager.update_employee(database)
        elif command == 7:
            sys.exit()
        else:
            print ("Invalid command!")


def main():
    database = CreateCompany()

    print ("Menu:")
    print ("1. Prints out all employees.")
    print ("2. Prints out the total sum for monthly spending that the company is doing for salaries")
    print ("3. Prints out the total sum for one year of operation (Again, salaries)")
    print ("4. Create a new employee.")
    print ("5. Delete the given employee from the database.")
    print ("6. The program should prompt the user to change each of the fields for the given employee.")
    print ("7. Exit.")

    cmd = CompanyManager()
    cmd.get_command(database, command)


if __name__ == '__main__':
    main()
