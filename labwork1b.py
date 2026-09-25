import random
from datetime import date, timedelta
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
#course list
courses = [
    {
        "id": "001",
        "name": "random course 1"
    },
    {
        "id": "002",
        "name": "random course 2"
    },
    {
        "id": "003",
        "name": "random course 3"
    }
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
    student = {
        "id": student_id,
        "name": name,
        "dob": dob.strftime("%d/%m/%Y")
    }
    return student
#generate a list of students
def generate_students():
    students = []
    used_ids = set()

    i = int(input("Enter the number of students: "))

    if i <= 0:
        print("Number of students must be greater than 0.")
        return students
    if i > 100:
        print("Number of students must be less than or equal to 100.")
        return students
    for j in range(i):
        student = generate_student(used_ids)
        students.append(student)
    return students
#generate marks
def generate_marks(students):
    marks = {}

    for course in courses:
        course_id = course["id"]
        marks[course_id] = {}
        for student in students:
            student_id = student["id"]
            #ramdom mark between 0 and 20
            mark = random.randint(0, 200) / 10
            marks[course_id][student_id] = mark
    return marks
#list students
def list_students(students):
    print("\n======= STUDENTS LIST =======")
    for student in students:
        print(
            student["id"],
            '',
            student["name"],
            '',
            student["dob"]
        )
#course list
def list_courses():
    print("\n======= COURSES LIST =======")
    for course in courses:
        print(
            course["id"],
            '',
            course["name"]
        )
#show marks
def show_marks(marks, students):
    print("\n======= MARKS LIST =======")
    for course in courses:
        print(
            course["id"],
            '',
            course["name"]
        )
    course_id = input("Enter course ID to show marks: ")
    #find course
    course_name = ""
    for course in courses:
        if course["id"] == course_id:
            course_name = course["name"]
            break
    if course_name == "":
        print("Course not found.")
        return

    print("\n======= STUDENT MARKS ======= ")
    print("Course: ", course_name)

    for student in students:
        student_id = student["id"]
        student_name = student["name"]
        mark = marks[course_id][student_id]
        print(
            "ID: ", student_id,
            '',
            "Name: ", student_name,
            '',
            "Mark: ", mark
        )
#show all marks
def show_all_marks(marks, students):
    print("\n======= ALL MARKS =======")
    for student in students:
        print("\n", "ID: ", student["id"], '', "-", student["name"])
        for course in courses:
            course_id = course["id"]
            course_name = course["name"]
            mark = marks[course_id][student["id"]]
            print(
                "Course: ", course_name,
                '',
                "Mark: ", mark
            )
#main function
def main():
    students = []
    marks = {}
    while True:
        print("\n")
        print("======= STUDENT MANAGEMENT SYSTEM =======")
        print("1. Student List")
        print("2. Course List")
        print("3. Show Marks for a Course")
        print("4. Show All Marks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        #generate students
        if choice == "1":
            students = generate_students()
            list_students(students)
            #generate marks
            marks = generate_marks(students)
        #course list
        elif choice == "2":
            list_courses()
        #show marks for a course
        elif choice == "3":
            if not students:
                print("No students available. Please generate students first.")
                continue
            if not marks:
                print("No marks available. Please generate marks first.")
                continue
            else:
                show_marks(marks, students)
        #show all marks
        elif choice == "4":
            if not students:
                print("No students available. Please generate students first.")
                continue
            if not marks:
                print("No marks available. Please generate marks first.")
                continue
            else:
                show_all_marks(marks, students)
        #exit
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
