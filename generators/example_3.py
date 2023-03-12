import itertools


# Infinite Generator using expression form
squares = (x * x for x in itertools.count(1))

for s in squares:
    print(s)
    # Generator finished when yield are exhausted / generator is closed / memory overflows
    if s > 500:
        squares.close()
