def read_file():
    try:
        with open('numbers.txt', 'r', encoding='utf-8') as file:
            numbers = file.read().strip().split(",")
            for number in numbers:
                number = number.strip()
                if number:
                    print(number)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read.")

if __name__ == '__main__':
    read_file()