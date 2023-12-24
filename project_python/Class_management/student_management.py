import random

class StudentManagement:
    def __init__(self):
        self.student_data = [
            {'uid': 1232, 'std_name': 'john doe', 'email': 'example@gmail.com', 'course_selected': 'BTech CSE',
             'passing_year': 2027, 'starting_year': 2023, 'current_year': 2023},
            {'uid': 1215, 'std_name': 'jane doe', 'email': 'example1@gmail.com', 'course_selected': 'BTech CSE',
             'passing_year': 2027, 'starting_year': 2023, 'current_year': 2026}
        ]

    def get_student_by_name(self, student_name):
        for student in self.student_data:
            if student['std_name'].lower() == student_name.lower():
                return student
        return None

    def add_new_student(self, student_name):
        unique_id = self.generate_unique_id()
        email = input("Enter student email: ")
        allowed_courses = ['BTech CSE', 'Civil Engineering', 'Mechanical Engineering', 'Electrical Engineering']
        while True:
            course_selected = input(f"Enter course selected ({', '.join(allowed_courses)}): ")
            if course_selected in allowed_courses:
                break
            else:
                print("Invalid course selection. Please choose from the allowed courses.")

        passing_year = int(input("Enter passing year: "))
        starting_year = int(input("Enter starting year: "))

        new_student = {
            'uid': unique_id,
            'std_name': student_name,
            'email': email,
            'course_selected': course_selected,
            'passing_year': passing_year,
            'starting_year': starting_year
        }

        self.student_data.append(new_student)
        print(f"New student {student_name} added successfully.")

    def generate_unique_id(self):
        while True:
            unique_id = random.randint(1000, 9999)
            if all(student['uid'] != unique_id for student in self.student_data):
                return unique_id