import sys

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read.")

    return content

def write_file(content, file):
    exec(open('settings.py').read(), globals())

    result = content.format(**globals())
    html = file.replace('.template', '.html')
    with open(html, 'w', encoding='utf-8') as f:
        f.write(result)

def main():
    if len(sys.argv) != 2:
        print("Error: invalid number of arguments.")
        sys.exit(1)
    
    if not sys.argv[1].endswith(".template") or sys.argv[1].rfind(".template") != sys.argv[1].find(".template"):
        print("Error: invalid file format.")
        sys.exit(1)

    content = read_file(sys.argv[1])
    write_file(content, sys.argv[1])

if __name__ == '__main__':
    main()