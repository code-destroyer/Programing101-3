import sqlite3


class CreateCompany:

    def __init__(self):
        self.db = sqlite3.connect("employees.db", timeout=10)
        self.cursor = self.db.cursor()
        self.db.commit()
        # self.db.row_factory = sqlite3.Row

    def create_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS company(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(256),
                monthly_salary INTEGER,
                yearly_bonus INTEGER,
                position VARCHAR(50))''')

    def insert_in_database(self):
        self.cursor.execute('''
            INSERT INTO company(id, name, monthly_salary, yearly_bonus, position) VALUES
                (1, "Ivan Ivanov", 5000, 10000, "Software Developer"),
                (2, "Rado Rado", 500, 0, "Technical Support Intern"),
                (3, "Ivo Ivo", 10000, 100000, "CEO"),
                (4, "Petar Petrov", 3000, 1000, "Marketing Manager"),
                (5, "Maria Georgieva", 8000, 10000, "COO")''')
        self.db.commit()
