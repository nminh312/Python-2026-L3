import curses
from domains import Course
from input import (generate_students, generate_marks)
from output import (list_students, list_courses, show_marks, show_all_marks,
                    show_gpa, sort_students_by_gpa)
#course list
courses = [
   Course("001", "course 1", 3),
   Course("002", "course 2", 3),
   Course("003", "course 3", 4),
]
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
            marks = generate_marks(students, courses)
            list_students(screen, students)
        elif choice == "2":
            list_courses(screen, courses)
        #show marks for a course
        elif choice == "3":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_marks(screen, marks, students, courses)
        #show all marks
        elif choice == "4":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_all_marks(screen, marks, students, courses)
        #show gpa
        elif choice == "5":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_gpa(screen, marks, students, courses)
        #sort students by gpa
        elif choice == "6":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                sort_students_by_gpa(students, marks, screen, courses)
        #exit
        elif choice == "7":
            break
        else:
            screen.addstr("Invalid choice. Please try again.")
            screen.refresh()
            screen.getch()
if __name__ == "__main__":
    curses.wrapper(main)