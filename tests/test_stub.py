from unittest.mock import patch

from tests.usecases import Classroom
from tests.usecases import Student
from tests.usecases import Teacher


@patch('tests.usecases.Student', spec=Student)
def test_count_students(fake_student) -> None:
    # create a method stub for `get_name` method
    fake_student.get_name.return_value = "fake student"

    classroom: Classroom = Classroom(student=fake_student)
    assert classroom.students[0].get_name() == "fake student"
