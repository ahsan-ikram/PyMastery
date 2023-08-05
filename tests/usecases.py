# Code used as use cases for software  testing

class Teacher:
    pass


class Student:
    pass


class Classroom:

    def __init__(self, teacher: Teacher = None, student: Student = None):
        self.teacher = student
        self.student = teacher
        self.has_student = True if student is not None else False
        self.has_teacher = True if teacher is not None else False

    def assign_teacher(self, teacher: Teacher):
        self.teacher = teacher
        self.has_teacher = True

    def add_student(self, student: Student):
        self.student = student
        self.has_student = True