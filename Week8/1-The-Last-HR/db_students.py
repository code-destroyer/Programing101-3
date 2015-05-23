import sqlite3


class CreateDB:

    def __init__(self):
        self.db = sqlite3.connect("db_student.db")
        self.cursor = self.db.cursor()

    def create_database(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Students(
                student_id INTEGER PRIMARY KEY,
                student_name TEXT,
                student_github TEXT)""")

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Courses(
                course_id INTEGER PRIMARY KEY,
                course_name TEXT)
                ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student_To_Course(
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES Students(student_id),
                FOREIGN KEY(course_id) REFERENCES Courses(course_id))''')


        self.db.commit()

# d = CreateDB()
# d.create_database()
