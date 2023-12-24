from Class_management.student_management import *
from Class_management.course_management import *
from Class_management.attendance_management import *
from Class_management.academic_report import *

student_manager = StudentManagement()
course_manager = CourseManagement(student_manager)

search_name = input("Enter the student name to search: ")
found_student = student_manager.get_student_by_name(search_name)
if found_student:
    print("Student found:")
    for key, value in found_student.items():
        print(f"{key}: {value}")
    print("current_year: ", found_student)
    if found_student['current_year'] - 3 == found_student['starting_year']:
        course_manager.select_specialization(found_student)
    print(found_student)
else:
    print("Student not found. Adding a new student.")
    student_manager.add_new_student(search_name)


attendance_manager = AttendanceManagement(student_manager.student_data)
search_name = input("Enter the student name to calculate attendance: ")
attendance_manager.calculate_attendance(search_name)


academic_report_manager = AcademicReport(student_manager.student_data)
search_name = input("Enter the student name to generate an academic report: ")
academic_report_manager.generate_academic_report(search_name)