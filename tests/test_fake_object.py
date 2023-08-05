"""
Test Doubles

- Dummy objects
- Fake objects
- Stubs
- Spies
- Mocks
"""

from unittest.mock import patch


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


@patch('tests.test_fake_object.Teacher', spec=Teacher)
@patch('tests.test_fake_object.Student', spec=Student)
def test_classroom_has_teacher(fake_student, fake_teacher) -> None:
    """ Mind the reverse order of assignment
    """
    classroom: Classroom = Classroom()
    assert classroom.has_teacher is False
    assert classroom.has_student is False

    classroom.assign_teacher(fake_teacher)
    classroom.add_student(fake_student)

    assert classroom.has_teacher is True
    assert classroom.has_student is True
