"""
#improved version
import os

def read_file(file_name):
    with open(file_name, 'r') as f:
        print('Current content of the file:')
        return f.read()
    
def write_file(file_name,content):
    #just created and writed the file
    with open(file_name, 'w') as f:
        f.write(content)

def user_input():
    print('\nEnter your text (type SAVE on a new line to save and exit):')
    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)
    return '\n'.join(lines)

def main():
    file_name = input('Enter the file name to open or create:')
    try:
        if os.path.exists(file_name):
            print(read_file(file_name))
        else:
            #open a file without writing anything to it
            write_file(file_name,'')

        content = user_input()
        write_file(file_name,content)
        print(f'{file_name} saved')
    except OSError:
        print(f'{file_name} could not be opened')

if __name__ == '__main__':
    main()

"""
import os
#My version
def create_file(file_name):
    with open(file_name, 'r') as f:
        print('Current content of the file:')
        return f.read()

def open_file(file_name,content):
    with open(file_name, 'a') as f:
        return f.write(content)

def get_user_input(file_name):
    print('Enter your text (type SAVE on a new line to save and exit):')
    lines = []
    text = input()
    while text != 'SAVE':
        lines.append(text)
        text = input()
    print(f'{file_name} saved')
    return '\n'.join(lines)    

def main():
    while True:
        try:
            file_name = input('Enter the file name to open or create:)')
            if os.path.exists(file_name):
                print(create_file(file_name))
            else:
                open_file(file_name,content='')

            if file_name == '' or file_name.startswith('/'):
                raise ValueError
            break
        except ValueError:
            print('Value erreor')

    open_file(file_name,get_user_input(file_name))

if __name__ == '__main__':
    main()

