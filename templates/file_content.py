def file_content_in_chunks(file, chunk_size=64):
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        yield data


def file_content_once(file):
    return file.readlines()


def main():
    with open('../resources/sample.txt', 'r+') as file:
        print('__________________________')
        print(f'READING DATA IN SINGLE CHUNK:')
        print(file_content_once(file))

    with open('../resources/sample.txt', 'r+') as file:
        for i, chunk in enumerate(file_content_in_chunks(file)):
            print('__________________________')
            print(f'ITERATION {i} DATA CHUNK:')
            print(chunk)


if __name__ == '__main__':
    main()
