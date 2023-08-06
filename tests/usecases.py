import random

import requests
from requests import Response

""" Code used as use cases for software  testing
"""


class Teacher:
    def __init__(self, name):
        self.name = name

    def compute_salary(self):
        return random.randint(len(self.name), 1000)


class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


STUDENT = Student("haroon")


def get_student_name() -> str:
    return STUDENT.name


class Classroom:

    def __init__(self, teacher: Teacher = None, student: Student = None):
        self.teacher = teacher
        self.students = [] if student is None else [student]
        self.has_student = False if student is None else True
        self.has_teacher = False if teacher is None else True

    def assign_teacher(self, teacher: Teacher):
        self.teacher = teacher
        self.has_teacher = True

    def add_student(self, student: Student):
        self.students.append(student)
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
