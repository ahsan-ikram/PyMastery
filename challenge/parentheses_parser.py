""" A parser of parenthesis validating / invalidating opening and closing parentheses in a large data file 1TB """
from templates.file_content import file_content_in_chunks

opening_parentheses = ['{', '(', '[']
closing_parentheses = ['}', ')', ']']
stack = []


def mirror_parentheses(first_parenthesis: str, second_parenthesis: str) -> bool:
    if first_parenthesis == '{' and second_parenthesis == '}':
        return True
    elif first_parenthesis == '}' and second_parenthesis == '{':
        return True
    if first_parenthesis == '(' and second_parenthesis == ')':
        return True
    elif first_parenthesis == ')' and second_parenthesis == '(':
        return True
    if first_parenthesis == '[' and second_parenthesis == ']':
        return True
    elif first_parenthesis == ']' and second_parenthesis == '[':
        return True
    return False


def validate_expression(expression: str) -> bool:
    for character in expression:
        if character in opening_parentheses:
            stack.append(character)

        if character in closing_parentheses:
            if len(stack) == 0 or (not mirror_parentheses(stack.pop(), character)):
                return False
    return True


def parse() -> bool:
    with open('../resources/expression.txt', 'r+') as file:
        for expression in file_content_in_chunks(file):
            if not validate_expression(expression):
                return False

    return True if len(stack) == 0 else False


def main():
    print(f'Expression file is Valid? {parse()}')


if __name__ == '__main__':
    main()
