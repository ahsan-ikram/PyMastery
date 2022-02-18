import time


def populate_distribution(lines):
    start = time.perf_counter()
    distribution = {}
    for line in lines:
        for word in line.replace('\n', '').split(' '):
            distribution[word] = distribution.setdefault(word, 0) + 1
    print(distribution)
    end = time.perf_counter()
    print(end - start)


def main():
    with open('sample.txt', 'r+') as file:
        populate_distribution(file.readlines())


if __name__ == '__main__':
    main()
