import csv
import os
import re
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))

def file_path(filename):
    return os.path.join(base_dir, filename)

#export data to csv file
def export_csv_file(students, courses, marks):
    #students csv
    with open(file_path("students.csv"), "w",
              newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "name", "dob"])
        writer.writeheader()
        for student in students:
            writer.writerow({
                "id": student.id,
                "name": student.name,
                "dob": student.dob})
    #courses csv
    with open(file_path("courses.csv"), "w",
              newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "name", "credits"])
        writer.writeheader()
        for course in courses:
            writer.writerow({
                "id": course.id,
                "name": course.name,
                "credits": course.credits})
    #marks csv
    with open(file_path("marks.csv"), "w",
              newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["student_id", "student_name",
                           "course_id", "course_name", "mark"])
        writer.writeheader()
        for course in courses:
            course_marks = marks.get(course.id, {})
            for student in students:
                if student.id in course_marks:
                    writer.writerow({
                        "student_id": student.id,
                        "student_name": student.name,
                        "course_id": course.id,
                        "course_name": course.name,
                        "mark": course_marks[student.id]})
#load csv files into pandas dataframes
def load_csv_files():
    students_df = pd.read_csv(
        file_path("students.csv"),
        dtype={"id": str, "name": str, "dob": str}
    )

    courses_df = pd.read_csv(
        file_path("courses.csv"),
        dtype={"id": str, "name": str}
    )

    marks_df = pd.read_csv(
        file_path("marks.csv"),
        dtype={
            "student_id": str,
            "student_name": str,
            "course_id": str,
            "course_name": str
        }
    )

    return students_df, courses_df, marks_df

#run a query on the students dataframe
def query_students(student_df, condition):
    condition = condition.strip()

    #convert = to == for pd
    condition = re.sub(
        r"(?<![<>=!])=(?!=)",
        "==",
        condition
    )

    #allow only simple comparisons on student columns
    allowed_condition = re.fullmatch(
        r"""(?:id|name|dob)\s*(?:==|!=)\s*(?:"[^"]*"|'[^']*')""",
        condition
    )

    if allowed_condition is None:
        raise ValueError(
            'Use a condition such as "name = "Nguyen Van A"", "id = "2XXXXXX"", "dob..."'
            "Allowed columns: id, name, dob\n"
            "Put text values in quotes."
        )

    return student_df.query(condition)
