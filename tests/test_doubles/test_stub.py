from unittest.mock import patch

from tests.usecases import Classroom
from tests.usecases import Student


@patch('tests.usecases.Student', spec=Student)
def test_count_students(fake_student) -> None:
    # Stub for "get_name" method
    fake_student.get_name.return_value = "fake student"

    classroom: Classroom = Classroom(student=fake_student)
    assert classroom.students[0].get_name() == "fake student"
