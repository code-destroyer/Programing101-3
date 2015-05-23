import sqlite3


class List_sth:

    def __init__(self):
        self.db = sqlite3.connect("db_student.db", timeout=10)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.db.execute("PRAGMA busy_timeout = 30000")

    def list_students(self):
        self.cursor.execute('''SELECT student_name, student_github
                                FROM Students''')
        for row in self.cursor:
            print('Student name: {} - GitHub: {}'.format(row["student_name"], row["student_github"]))

    def list_courses(self):
        self.cursor.execute('''SELECT * FROM Courses''')
        for row in self.cursor:
            print('{} {}'.format(row["course_id"], row["course_name"]))

    def list_students_to_courses(self):
        self.cursor.execute('''SELECT student_name, course_name
                                FROM Students, Courses, Student_to_Course
                                WHERE students.student_id = student_to_course.student_id
                                AND courses.course_id = student_to_course.course_id''')
        for row in self.cursor:
            print('Student: {} - Course: {}'.format(row["student_name"], row["course_name"]))

    def list_student_with_most_courses(self):
        self.cursor.execute('''SELECT student_name, COUNT(student_to_course.student_id)
                                FROM Students, Student_to_Course
                                WHERE students.student_id = student_to_course.student_id
                                GROUP BY students.student_id
                                ORDER BY COUNT(students.student_id)
                                DESC LIMIT 10''')
        rows = self.cursor.fetchall()
        print('TOP 10 students with most attended courses:')
        for row in rows:
            print('{} - {}'.format(row['student_name'], row['COUNT(student_to_course.student_id)']))


def main():
    list_sth = List_sth()
    list_sth.list_students()
    # list_sth.list_courses()
    # list_sth.list_students_to_courses()
    # list_sth.list_student_with_most_courses()

if __name__ == '__main__':
    main()
