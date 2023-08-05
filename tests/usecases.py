import requests
from requests import Response

""" Code used as use cases for software  testing
"""


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


def third_party_dependency() -> int:
    url = "https://www.google.com"
    try:
        response: Response = requests.get(url, timeout=2.50)
        return response.status_code
    except requests.exceptions.HTTPError as http_error:
        print("Http Error:", http_error)
    except requests.exceptions.ConnectionError as connection_error:
        print("Error Connecting:", connection_error)
    except requests.exceptions.Timeout as timeout_error:
        print("Timeout Error:", timeout_error)
    except requests.exceptions.RequestException as request_error:
        print("Oh No!: Something Else", request_error)
    return -1


def api_response() -> str:
    return "success" if third_party_dependency() == 200 else "failure"
