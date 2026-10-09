import curses
import numpy as np

#list students
def list_students(screen, students):
    screen.clear()
    screen.addstr(0, 0, "======= STUDENTS LIST =======\n")
    screen.refresh()
    for student in students:
        screen.addstr(
            f"ID: {student.id}\n"
            f"Name: {student.name}\n"
            f"DOB: {student.dob}\n"
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
def list_courses(screen, courses):
    screen.clear()
    screen.addstr(0, 0, "======= COURSES LIST =======\n")
    for course in courses:
        screen.addstr(
            f"ID: {course.id}\n"
            f"Name: {course.name}\n"
            f"Credits: {course.credits}\n"
            "---------------------------------\n"
        )
    screen.addstr("\nPress any key to continue...")
    screen.getch()
#show marks for 1 course
def show_marks(screen, marks, students, courses):
    screen.clear()
    screen.addstr(0, 0, "======= MARKS LIST =======\n")
    for course in courses:
        screen.addstr(
            f"ID: {course.id}\n"
            f"Name: {course.name}\n"
            f"Credits: {course.credits}\n"
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
        if course.id == course_id:
            course_name = course.name
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
        student_id = student.id
        student_name = student.name
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
def show_all_marks(screen, marks, students, courses):
    screen.clear()
    screen.addstr(0, 0, "======= ALL MARKS =======\n")
    screen.refresh()

    for student in students:
        student_id = student.id
        student_name = student.name

        screen.addstr(
            f"ID: {student_id}\n"
            f"Name: {student_name}\n"
        )
        for course in courses:
            course_id = course.id
            course_name = course.name
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
def cal_gpa(student_id, marks, courses):
    student_marks = []
    student_credits = []
    for course in courses:
        course_id = course.id
        mark = marks[course_id][student_id]
        credits = course.credits
        student_marks.append(mark)
        student_credits.append(credits)
    marks_array = np.array(student_marks)
    credits_array = np.array(student_credits)
    weighted_sum = np.sum(marks_array * credits_array)
    total_credits = np.sum(credits_array)
    gpa = weighted_sum / total_credits
    return gpa
#show gpa
def show_gpa(screen, marks, students, courses):
    screen.clear()
    screen.addstr(0, 0, "======= GPA LIST =======\n")
    screen.refresh()

    for student in students:
        student_id = student.id
        student_name = student.name
        gpa = cal_gpa(student_id, marks, courses)
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
def sort_students_by_gpa(students, marks, screen, courses):
    sorted_students = []

    for student in students:
        student_id = student.id
        gpa = cal_gpa(student_id, marks, courses)
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
            f"ID: {student.id}\n"
            f"Name: {student.name}\n"
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
