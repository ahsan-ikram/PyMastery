from unittest.mock import patch, PropertyMock

from tests.usecases import Classroom
from tests.usecases import Student
from tests.usecases import Teacher


@patch('tests.usecases.Teacher', spec=Teacher)
@patch('tests.usecases.Student', spec=Student)
def test_classroom_both_teacher_student(fake_student, fake_teacher) -> None:
    """ Testing with fake objects and properties. Mind the reverse order of assignment """

    classroom: Classroom = Classroom()
    assert classroom.has_teacher is False
    assert classroom.has_student is False

    classroom.assign_teacher(fake_teacher)
    classroom.add_student(fake_student)

    assert classroom.has_teacher is True
    assert classroom.has_student is True

    # Add a fake property to the teacher
    type(fake_student).name = PropertyMock(return_value="fake property")
    assert "fake property" == fake_student.name

