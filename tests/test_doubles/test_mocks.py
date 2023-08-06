from unittest.mock import patch

import tests.usecases
from tests.usecases import api_response, Teacher, Student, get_student_name


def test_mocking_an_object(mocker):
    """ Mocking a constant / object"""
    mocker.patch.object(tests.usecases, 'STUDENT', Student("hashim"))
    assert "hashim" == get_student_name()


def test_api_response_using_mocked_third_party_dependency(mocker):
    """ Mocking a function (third_party_dependency()) defined in tests.usecases """
    mocker.patch('tests.usecases.third_party_dependency', return_value=200)
    assert "success" == api_response()


@patch("tests.usecases.third_party_dependency")
def test_api_response_using_patch_decorator(mocker):
    """ Mocking a function (third_party_dependency()) defined in tests.usecases using decorator syntax """
    mocker.return_value = -1
    assert "failure" == api_response()


# Mocking a class method
def test_mocking_class_method(mocker):
    """ Mocking a class method (Teacher.compute_salary) of class "Teacher" """
    def mock_salary(*args):
        """
        The difference with stub is that stub only is concerned with return value
        therefore dynamically computed value will not work. Whereas using mocks for
        function may incorporate dynamically computed values.
        """
        return 0

    expected = 0

    mocker.patch('tests.usecases.Teacher.compute_salary', mock_salary)
    actual = Teacher("John").compute_salary()
    assert expected == actual
