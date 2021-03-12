class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_lecturer = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, student, course, grade):
        if isinstance(student, Student) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if grade <= 10:
                student.grades_lecturer.append(grade)
            else:
                return 'Оценка выставляется по 10 балльной шкале'
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade, reviewer):
        if isinstance(reviewer, Reviewer) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Andrey', 'Chebunin')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10, cool_reviewer)
cool_reviewer.rate_hw(best_student, 'Python', 10, cool_reviewer)
cool_reviewer.rate_hw(best_student, 'Python', 10, cool_reviewer)

best_lecturer = Lecturer('Olga', 'Voronina')
best_lecturer.courses_attached += ['Python']
best_student.rate_lecturer(best_lecturer, best_student, 'Python', 10)
best_student.rate_lecturer(best_lecturer, best_student, 'Python', 10)
best_student.rate_lecturer(best_lecturer, best_student, 'Python', 10)


print(best_student.grades)
print(best_student.grades_lecturer)
