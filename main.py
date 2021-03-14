class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        for grade in self.grades.values():
            self.score = grade

        for courses_p in self.courses_in_progress:
            self.courses_progress = courses_p

        if len(self.finished_courses) == 0:
            self.courses_finished = 'Завершенные курсы отсутствуют.'
        else:
            for courses_f in self.finished_courses:
                self.courses_finished = courses_f

        self.rating = round(sum(self.score) / len(self.score), 1)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.rating}\n' \
               f'Курсы в процессе изучения: {self.courses_progress}\n' \
               f'Завершенные курсы: {self.courses_finished}'

    def __gt__(self, other):
        return self.rating > other.rating

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, student, course, grade):
        if isinstance(student, Student) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if 10 >= grade >= 1:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Оценка выставляется по 10 балльной шкале'
        else:
            return 'Ошибка'

    def grade_calculation(self, students, course):
        for key, value in self.grades.items():
            if course in key:
                return round(sum(value) / len(students), 1)

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
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        for grades in self.grades.values():
            self.score = grades

        self.rating = round(sum(self.score) / len(self.score), 1)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating}'

    def __gt__(self, other):
        return self.rating > other.rating

    def grade_calculation(self, lecturers, course):
        for key, value in self.grades.items():
            if course in key:
                return round(sum(value) / len(lecturers), 1)


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


first_student = Student('Christopher', 'Carroll', 'Man')
second_student = Student('Linda', 'Watson', 'Woman')
first_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Java']
first_student.add_courses('C++')

first_lecturer = Lecturer('Richard', 'Austin')
second_lecturer = Lecturer('Amanda', 'Henry')
first_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Java']

first_reviewer = Reviewer('Laura', 'Perez')
second_reviewer = Reviewer('Everett', 'Sanders')
first_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Java']

first_student.rate_lecturer(first_lecturer, first_student, 'Python', 10)
second_student.rate_lecturer(second_lecturer, second_student, 'Java', 9)
first_reviewer.rate_hw(first_student, 'Python', 10, first_reviewer)
second_reviewer.rate_hw(second_student, 'Java', 9, second_reviewer)

print(first_student)
print(first_student > second_student)  # Возникает ошибка, но если принтовать с консоли то все ок.
print(first_lecturer)
print(first_lecturer > second_lecturer)  # Возникает ошибка, но если принтовать с консоли то все ок.
print(first_reviewer)
