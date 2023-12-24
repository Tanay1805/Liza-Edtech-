class CourseManagement:
    def __init__(self, student_manager):
        self.student_manager = student_manager
        self.specialization_options = {
            'BTech CSE': ['Machine Learning', 'Network Security', 'Data Science'],
            #Dusre course Daalne h
        }

    def select_specialization(self, student):
        course_selected = student['course_selected']
        if student['current_year'] - 3 == student['starting_year']:
            valid_specializations = self.specialization_options.get(course_selected, [])
            
            while True:
                print(f"Specialization options for {course_selected}: {', '.join(valid_specializations)}")
                specialization = input("Select a specialization: ")

                if specialization in valid_specializations:
                    student['specialization_course'] = specialization
                    print(f"Specialization course {specialization} selected for {student['std_name']}.")
                    break
                else:
                    print(f"Invalid specialization. Please select from the available options.")