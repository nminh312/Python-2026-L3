import random
from datetime import date, timedelta
import numpy as np
import math
import curses
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
        "name": "random course 1",
        "credits": 3
    },
    {
        "id": "002",
        "name": "random course 2",
        "credits": 3
    },
    {
        "id": "003",
        "name": "random course 3",
        "credits": 4
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
def generate_students(number):
    students = []
    used_ids = set()

    for j in range(number):
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
            #round mark to 1 decimal place
            mark = math.floor(mark * 10) / 10
            marks[course_id][student_id] = mark
    return marks
#list students
def list_students(screen, students):
    screen.clear()
    screen.addstr(0, 0, "======= STUDENTS LIST =======\n")
    screen.refresh()
    for student in students:
        screen.addstr(
            f"ID: {student['id']}\n"
            f"Name: {student['name']}\n"
            f"DOB: {student['dob']}\n"
            "---------------------------------\n"
        )
        #if screen full
        y, x = screen.getyx()
        max_y, max_x = screen.getmaxyx()
        if y >= max_y - 2:
            screen.addstr("\nPress any key for more...")
            screen.getch()
            screen.clear()
            screen.addstr(0, 0, "======= STUDENTS LIST =======\n")
            screen.refresh()
    screen.addstr("\nPress any key to continue...")
    screen.refresh()
    screen.getch()
#course list
def list_courses(screen):
    screen.clear()
    screen.addstr(0, 0, "======= COURSES LIST =======\n")
    for course in courses:
        screen.addstr(
            f"ID: {course['id']}\n"
            f"Name: {course['name']}\n"
            f"Credits: {course['credits']}\n"
            "---------------------------------\n"
        )
    screen.addstr("\nPress any key to continue...")
    screen.getch()
#show marks
def show_marks(screen, marks, students):
    screen.clear()
    screen.addstr(0, 0, "======= MARKS LIST =======\n")
    for course in courses:
        screen.addstr(
            f"ID: {course['id']}\n"
            f"Name: {course['name']}\n"
            f"Credits: {course['credits']}\n"
            "---------------------------------\n"
        )
    screen.addstr("\nEnter course ID: ")
    screen.refresh()
    curses.echo()
    course_id = screen.getstr().decode('utf-8').strip()
    curses.noecho()
    #find course
    course_name = ""
    for course in courses:
        if course["id"] == course_id:
            course_name = course["name"]
            break
    if course_name == "":
        screen.addstr("Course not found.")
        screen.refresh()
        screen.getch()
        return

    screen.clear()
    screen.addstr(f"\n======= STUDENT MARKS ======= ")
    screen.addstr(f"Course: {course_name}\n")
    screen.refresh()

    for student in students:
        student_id = student["id"]
        student_name = student["name"]
        mark = marks[course_id][student_id]
        screen.addstr(
            f"ID: {student_id}\n"
            f"Name: {student_name}\n"
            f"Mark: {mark:.1f}\n"
        )
        #if screen full
        y, x = screen.getyx()
        max_y, max_x = screen.getmaxyx()
        if y >= max_y - 2:
            screen.addstr("\nPress any key for more...")
            screen.getch()
            screen.clear()
            screen.addstr(f"\n======= STUDENT MARKS ======= ")
            screen.addstr(f"Course: {course_name}\n")
            screen.refresh()
    screen.addstr("\nPress any key to continue")
    screen.getch()
#show all marks
def show_all_marks(screen, marks, students):
    screen.clear()
    screen.addstr(0, 0, "======= ALL MARKS =======\n")
    screen.refresh()

    for student in students:
        student_id = student["id"]
        student_name = student["name"]

        screen.addstr(
            f"ID: {student_id}\n"
            f"Name: {student_name}\n"
        )
        for course in courses:
            course_id = course["id"]
            course_name = course["name"]
            mark = marks[course_id][student_id]
            screen.addstr(
                f"Course: {course_name}\n"
                f"Mark: {mark:.1f}\n"
            )
        screen.addstr("---------------------------------\n")
        #if screen full
        y, x = screen.getyx()
        max_y, max_x = screen.getmaxyx()
        if y >= max_y - 6:
            screen.addstr("\nPress any key for more...")
            screen.refresh()
            screen.getch()
            screen.clear()
            screen.addstr(0, 0, "======= ALL MARKS =======\n")
            screen.refresh()
    screen.addstr("\nPress any key to continue...")
    screen.refresh()
    screen.getch()
#caculate gpa
def cal_gpa(student_id, marks):
    student_marks = []
    student_credits = []
    for course in courses:
        course_id = course["id"]
        mark = marks[course_id][student_id]
        credits = course["credits"]
        student_marks.append(mark)
        student_credits.append(credits)
    marks_array = np.array(student_marks)
    credits_array = np.array(student_credits)
    weighted_sum = np.sum(marks_array * credits_array)
    total_credits = np.sum(credits_array)
    gpa = weighted_sum / total_credits
    return gpa
#show gpa
def show_gpa(screen, marks, students):
    screen.clear()
    screen.addstr(0, 0, "======= GPA LIST =======\n")
    screen.refresh()

    for student in students:
        student_id = student["id"]
        student_name = student["name"]
        gpa = cal_gpa(student_id, marks)
        screen.addstr(
            f"ID: {student_id}\n"
            f"Name: {student_name}\n"
            f"GPA: {gpa:.2f}\n"
            "---------------------------------\n"
        )
        #if screen full
        y, x = screen.getyx()
        max_y, max_x = screen.getmaxyx()
        if y >= max_y - 5:
            screen.addstr("\nPress any key for more...")
            screen.refresh()
            screen.getch()
            screen.clear()
            screen.addstr(0, 0, "======= GPA LIST =======\n")
            screen.refresh()
    screen.addstr("\nPress any key to continue...")
    screen.getch()
#sort students by gpa
def sort_students_by_gpa(students, marks, screen):
    sorted_students = []

    for student in students:
        student_id = student["id"]
        gpa = cal_gpa(student_id, marks)
        sorted_students.append({
            "student": student,
            "gpa": gpa
        })
    #sort by gpa highest to lowest
    sorted_students.sort(key=lambda x: x["gpa"], reverse=True)

    screen.clear()
    screen.addstr(0, 0, "======= STUDENTS SORTED BY GPA =======\n")
    screen.refresh()

    position = 1
    for item in sorted_students:
        student = item["student"]
        gpa = item["gpa"]
        screen.addstr(
            f"Position: {position}\n"
            f"ID: {student['id']}\n"
            f"Name: {student['name']}\n"
            f"GPA: {gpa:.2f}\n"
            "---------------------------------\n"
        )
        position += 1
        #if screen full
        y, x = screen.getyx()
        max_y, max_x = screen.getmaxyx()
        if y >= max_y - 5:
            screen.addstr("\nPress any key for more...")
            screen.refresh()
            screen.getch()
            screen.clear()
            screen.addstr(0, 0, "======= STUDENTS SORTED BY GPA =======\n")
            screen.refresh()
    screen.addstr("\nPress any key to continue...")
    screen.refresh()
    screen.getch()
#main function
def main(screen):
    students = []
    marks = {}
    while True:
        screen.clear()
        screen.addstr(0, 0, "======= STUDENT MANAGEMENT SYSTEM =======\n")
        screen.addstr("1. Student List\n")
        screen.addstr("2. Course List\n")
        screen.addstr("3. Show Marks for a Course\n")
        screen.addstr("4. Show All Marks\n")
        screen.addstr("5. Show GPA\n")
        screen.addstr("6. Sort Students by GPA\n")
        screen.addstr("7. Exit\n")
        screen.addstr("Enter your choice: ")
        screen.refresh()
        
        curses.echo()
        choice = screen.getstr().decode('utf-8').strip()
        curses.noecho()
        
        #generate students
        if choice == "1":
            screen.clear()
            screen.addstr("Enter number of students: ")
            screen.refresh()
            curses.echo()
            try:
                number = int(screen.getstr().decode('utf-8').strip())
            except ValueError:
                curses.noecho()
                screen.addstr("Invalid number.") 
                screen.refresh()
                screen.getch()
                continue
            curses.noecho()
            if number <= 0:
                screen.addstr("Number must be greater than 0.")
                screen.refresh()
                screen.getch()
                continue
            students = generate_students(number)
            marks = generate_marks(students)
            list_students(screen, students)
        elif choice == "2":
            list_courses(screen)
        #show marks for a course
        elif choice == "3":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_marks(screen, marks, students)
        #show all marks
        elif choice == "4":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_all_marks(screen, marks, students)
        #show gpa
        elif choice == "5":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_gpa(screen, marks, students)
        #sort students by gpa
        elif choice == "6":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                sort_students_by_gpa(students, marks, screen)
        #exit
        elif choice == "7":
            break
        else:
            screen.addstr("Invalid choice. Please try again.")
            screen.refresh()
            screen.getch()
if __name__ == "__main__":
    curses.wrapper(main)