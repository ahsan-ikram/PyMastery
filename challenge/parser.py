def main():
    with open('sample.txt', 'r+') as file:
        lines = file.readlines()
        print(lines)


if __name__ == '__main__':
    main()
