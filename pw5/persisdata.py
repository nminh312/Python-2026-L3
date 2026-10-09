import json
import os
import zipfile
from domains import Student, Course

#keep the data in this file
base_dir = os.path.dirname(os.path.abspath(__file__))
text_files = ("students.txt", "courses.txt", "marks.txt")

def file_path(filename):
    return os.path.join(base_dir, filename)

#save all data sructures to text files
def save_text_files(students, courses, marks):
    with open(file_path("students.txt"), "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "id": student.id,
                    "name": student.name,
                    "dob": student.dob
                }
                for student in students
            ],
            f,
            indent=2
        )
    with open(file_path("courses.txt"), "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "id": course.id,
                    "name": course.name,
                    "credits": course.credits
                }
                for course in courses
            ],
            f,
            indent=2
        )
    with open(file_path("marks.txt"), "w", encoding="utf-8") as f:
        json.dump(marks, f, indent=2)
#compress the text files into students.dat
def compress_text_files(method_choice):
    methods = {
        "1":zipfile.ZIP_DEFLATED,
        "2":zipfile.ZIP_BZIP2,
        "3":zipfile.ZIP_LZMA
    }
    if method_choice not in methods:
        raise ValueError("Invalid compression method")
    with zipfile.ZipFile(
        file_path("students.dat"),
        "w",
        compression=methods[method_choice]
    ) as archive:
        for filename in text_files:
            archive.write(file_path(filename), arcname=filename)

#if students.dat exists, decompress and restore the saved data
def load_saved_data():
    archive_path = file_path("students.dat")
    if not os.path.exists(archive_path):
        return None
    with zipfile.ZipFile(archive_path, "r") as archive:
        for filename in text_files:
            archive.extract(filename, path=base_dir)
    with open(file_path("students.txt"), "r", encoding="utf-8") as f:
        students_data = json.load(f)
    with open(file_path("courses.txt"), "r", encoding="utf-8") as f:
        courses_data = json.load(f)
    with open(file_path("marks.txt"), "r", encoding="utf-8") as f:
        marks_data = json.load(f)

    students = [
        Student(item["id"], item["name"], item["dob"]) 
        for item in students_data
    ]
    courses = [
        Course(item["id"], item["name"], item["credits"]) 
        for item in courses_data
    ]
    return students, courses, marks_data