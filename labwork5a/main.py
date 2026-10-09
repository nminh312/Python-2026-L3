import curses
from domains import Course
from input import (generate_students, generate_marks)
from persisdata import (save_text_files, compress_text_files, load_saved_data,
                        save_pickle_file)
from csv_tool import (export_csv_file, load_csv_files, query_students)
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
    else:
        #generate students and marks if no saved data
            screen.clear()
            screen.addstr("Enter number of students: \n")
            screen.refresh()
            curses.echo()
            try:
                num_students = int(screen.getstr().decode('utf-8').strip())
                if num_students <= 0:
                    raise ValueError("Number of students must be positive.")
            except ValueError:
                curses.noecho()
                screen.addstr("Invalid number")
                screen.refresh()
                screen.getch()
                return
            curses.noecho()
            students = generate_students(num_students)
            marks = generate_marks(students, current_courses)

            #save data after generation
            save_text_files(students, current_courses, marks)
            save_pickle_file(students, current_courses, marks)

    while True:
        screen.clear()
        screen.addstr(0, 0, "======= STUDENT MANAGEMENT SYSTEM =======\n")
        screen.addstr("1. Student List\n")
        screen.addstr("2. Course List\n")
        screen.addstr("3. Show Marks for a Course\n")
        screen.addstr("4. Show All Marks\n")
        screen.addstr("5. Show GPA\n")
        screen.addstr("6. Sort Students by GPA\n")
        screen.addstr("7. Export CSV files\n")
        screen.addstr("8. Query students using Pandas\n")
        screen.addstr("9. Save and Exit\n")
        screen.addstr("Enter your choice: ")
        screen.refresh()
        
        curses.echo()
        choice = screen.getstr().decode('utf-8').strip()
        curses.noecho()
        
        #generate students
        if choice == "1":
            list_students(screen, students)
        elif choice == "2":
            list_courses(screen, current_courses)
        #show marks for a course
        elif choice == "3":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_marks(screen, marks, students, current_courses)
        #show all marks
        elif choice == "4":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_all_marks(screen, marks, students, current_courses)
        #show gpa
        elif choice == "5":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                show_gpa(screen, marks, students, current_courses)
        #sort students by gpa
        elif choice == "6":
            if not students or not marks:
                screen.addstr("No students or marks available.")
                screen.refresh()
                screen.getch()
            else:
                sort_students_by_gpa(students, marks, screen, current_courses)
        #export to csv
        elif choice == "7":
            if not students:
                screen.addstr("Make a student list first")
            else:
                try:
                    export_csv_file(
                        students, current_courses, marks
                    )
                    screen.clear()
                    screen.addstr("Exported!")
                except Exception as error:
                    screen.clear()
                    screen.addstr(f"CSV export failed: {error}")
                screen.refresh()
                screen.getch()
        #query using pd
        elif choice == "8":
            if not students:
                screen.addstr("Make a student list first")
                screen.refresh()
                screen.getch()
            else:
                #ensure csv data is up to date
                export_csv_file(
                    students, current_courses, marks
                )   
                #load the csv files into dataframes
                students_df, courses_df, marks_df =load_csv_files()
                screen.clear()
                screen.addstr(
                    'Enter a condition(e.g "name = "Nguyen Van A"")\n'
                )
                screen.addstr("Condition: ")
                screen.refresh()

                curses.echo()
                try:
                    condition = (
                        screen.getstr().decode("utf-8").strip()
                    )
                finally:
                    curses.noecho()
                try:
                    result = query_students(
                        students_df, condition
                    )
                    title = f"Mathcing students: {len(result)}"

                    if result.empty:
                        rows = ["No matching students"]
                    else:
                        rows = result.to_string(
                            index=False
                        ).splitlines()
                except Exception as error:
                    title = "Query failed"
                    rows = [str(error)]

                screen.clear()
                max_y, max_x = screen.getmaxyx()
                screen.addnstr(0, 0, title, max_x -1)

                for row_number, row in enumerate(
                    rows[:max_y -2], start=1
                ):
                    screen.addnstr(
                        row_number, 0, row, max_x -1
                    )
                screen.addnstr(
                    max_y -1, 0,
                    "Press any key to return to menu",
                    max_x -1
                )
                screen.refresh()
                screen.getch()
        #exit and saved data
        elif choice == "9":
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
                save_text_files(students, current_courses, marks)
                save_pickle_file(students, current_courses, marks)
                export_csv_file(students, current_courses, marks)
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