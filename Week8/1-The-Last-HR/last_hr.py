import requests
import json
import sqlite3


class LastHR:

    def __init__(self):
        self.courses_set = set()
        self.filename = "datadata.json"
        self.db = sqlite3.connect("db_student.db", timeout=10)
        self.cursor = self.db.cursor()
        self.db.execute("PRAGMA busy_timeout = 30000")
        self.course_name_to_id = {}

    def get_json(self, filename):
        self.response = requests.get("https://hackbulgaria.com/api/students/").json()
        with open(filename, 'w') as f:
            f.write(json.dumps(self.response, indent=True, ensure_ascii=False))

    def load_json(self, filename):
        with open("datadata.json") as f:
            self.json_data = json.load(f)

    def fill_courses(self):
        for students in self.json_data:
            for courses in students["courses"]:
                self.courses_set.add(courses["name"])
        for course in self.courses_set:
            self.cursor.execute('''INSERT INTO courses(course_name)
                                    VALUES(?)''', (course, ))
        self.current_courses = students["courses"]
        self.db.commit()
        return self.cursor.lastrowid

    def fill_students(self):
        for students in self.json_data:
            self.cursor.execute('''INSERT INTO students(student_name, student_github)
                                    VALUES(?,?)''', (students["name"], students["github"]))
        self.db.commit()
        return self.cursor.lastrowid

    def fill_third_table(self):
        st_co = set()
        for students in self.json_data:
            for course in students['courses']:
                self.cursor.execute('''SELECT student_id, course_id FROM Students, Courses
                                        WHERE student_name = ? AND course_name = ?''', (students['name'], course['name']))
                for row in self.cursor:
                    st_co.add(row)
        for r in st_co:
            self.cursor.execute('''INSERT INTO Student_to_Course(student_id, course_id)
                                    VALUES (?,?)''', (r[0], r[1]))
        self.db.commit()

json2 = LastHR()
json2.load_json("datadata.json")
# add = LastHR.fill_courses(json2)
# add2 = LastHR.fill_students(json2)
# add3 = LastHR.fill_third_table(json2)
