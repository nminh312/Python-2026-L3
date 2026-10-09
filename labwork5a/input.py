import random
from datetime import date, timedelta
import math
from domains import Student
#name list
first_name = [
    "Nguyen", "Tran", "Le", "Pham", "Hoang", "Phan", "Vu", "Dang", "Bui", "Do", "Ngo"
]

middle_name = [
    "Van", "Thi", "Duc", "Quang", "Huu", "Minh", "Thanh", "Tuan", "Anh", "Bao", "Khanh"
]

last_name = [
    "Anh", "Binh", "Chau", "Diem", "Giang", "Hien", "Khanh", "Linh", "Minh", "Ngoc", "Phuong"
]
#generate random date
def ramdom_date(year):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 28)

    days = (end_date - start_date).days
    random_days = random.randint(0, days)

    return start_date + timedelta(days=random_days)
#generate ID
def generate_student_id(year, used_ids):

    if year == 2006:
        prefix = "2410"
    else:
        prefix = "2510"
    while True:
        random_number = random.randint(100, 999)
        student_id = prefix + str(random_number)
        if student_id not in used_ids:
            used_ids.add(student_id)
            return student_id
#generate random student
def generate_student(used_ids):
    #choose birth year
    year = random.choice([2006, 2007])
    #generate student ID
    student_id = generate_student_id(year, used_ids)
    #generate random name
    first = random.choice(first_name)
    middle = random.choice(middle_name)
    last = random.choice(last_name)
    name = first + " " + middle + " " + last
    #generate random dob
    dob = ramdom_date(year)
    #create student dictionary
    student = Student(
        student_id,
        name,
        dob.strftime("%d/%m/%Y")
    )
    return student
#generate a list of students
def generate_students(number):
    students = []
    used_ids = set()

    for j in range(number):
        student = generate_student(used_ids)
        students.append(student)
    return students
#generate marks
def generate_marks(students, courses):
    marks = {}

    for course in courses:
        course_id = course.id
        marks[course_id] = {}
        for student in students:
            student_id = student.id
            #ramdom mark between 0 and 20
            mark = random.randint(0, 200) / 10
            #round mark to 1 decimal place
            mark = math.floor(mark * 10) / 10
            marks[course_id][student_id] = mark
    return marks
