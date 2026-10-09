import curses
from domains import Course
from input import (generate_students, generate_marks)
from persisdata import (save_text_files, compress_text_files, load_saved_data)
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

    current_courses = courses

    #load previously saved data if available
    saved_data = load_saved_data()
    if saved_data is not None:
        students, current_courses, marks = saved_data

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

            #save all data after generation
            save_text_files(students, courses, marks)

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
        #exit and saved data
        elif choice == "7":
            screen.clear()
            screen.addstr("=======SAVE AND EXIT=======\n")
            screen.addstr("Choose compression method:\n")
            screen.addstr("1. ZIP_DEFLATED\n")
            screen.addstr("2. ZIP_BZIP2\n")
            screen.addstr("3. ZIP_LZMA\n")
            screen.addstr("Enter your choice(1-3): ")
            screen.refresh()

            curses.echo()
            method_choice = screen.getstr().decode('utf-8').strip()
            curses.noecho()

            #check choice
            if method_choice not in ["1", "2", "3"]:
                screen.addstr("Invalid choice. Please try again.")
                screen.refresh()
                screen.getch()
                continue
            #save and compress data
            try:
                save_text_files(students, courses, marks)
                compress_text_files(method_choice)
                screen.addstr("\nData saved and compressed to students.dat successfully.")
                screen.addstr("\nPress any key to exit.")
                screen.refresh()
                screen.getch()
                break
            except Exception as error:
                screen.addstr(f"\nError saving or compressing data: {error}")
                screen.addstr("\nPress any key to return.")
                screen.refresh()
                screen.getch()
                continue
        else:
            screen.addstr("Invalid choice. Please try again.")
            screen.refresh()
            screen.getch()
if __name__ == "__main__":
    curses.wrapper(main)