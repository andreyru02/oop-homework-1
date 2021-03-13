class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        name = self.name
        surname = self.surname

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
        name = self.name
        surname = self.surname

        for grades in self.grades.values():
            self.score = grades

        self.rating = round(sum(self.score) / len(self.score), 1)
        return f'Имя: {name}\nФамилия: {surname}\nСредняя оценка за лекции: {self.rating}'

    def __gt__(self, other):
        return self.rating > other.rating


class Reviewer(Mentor):
    def __str__(self):
        name = self.name
        surname = self.surname
        return f'Имя: {name}\nФамилия: {surname}'


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

lecturer = Lecturer('User', 'User')
lecturer.courses_attached += ['Python']

best_student.rate_lecturer(lecturer, best_student, 'Python', 9)
best_student.rate_lecturer(lecturer, best_student, 'Python', 10)
best_student.rate_lecturer(lecturer, best_student, 'Python', 10)

print(best_student.grades)
print(best_lecturer.grades)
print(cool_reviewer)
print(best_lecturer)
print(best_student)
