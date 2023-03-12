import string


def letters():
    for c in string.ascii_lowercase:
        yield c


# Generates letter during each loop iteration
for letter in letters():
    print(letter)
