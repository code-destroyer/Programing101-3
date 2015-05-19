import sqlite3


class CreateCompany:

    def __init__(self):
        self.db = sqlite3.connect("create_company.db")
        self.cursor = self.db.cursor()

    def create_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS company(
                id INT UNSIGNED NOT NULL PRIMARY KEY,
                name VARCHAR(256) NOT NULL,
                monthly_salary INT UNSIGNED NULL,
                yearly_bonus INT UNSIGNED NULL,
                position VARCHAR(50) NOT NULL)''')

    def insert_in_database(self):
        self.cursor.execute('''
            INSERT INTO company(id, name, monthly_salary, yearly_bonus, position) VALUES
                (1, "Ivan Ivanov", 5000, 10000, "Software Developer"),
                (2, "Rado Rado", 500, 0, "Technical Support Intern"),
                (3, "Ivo Ivo", 10000, 100000, "CEO"),
                (4, "Petar Petrov", 3000, 1000, "Marketing Manager"),
                (5, "Maria Georgieva", 8000, 10000, "COO")''' )
        self.db.commit()
