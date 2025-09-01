def show_list():
    print()
    print("To-do List Menu:")
    list_menu = ["View Task","Add a Task","Remove a Task","Exit"]
    for index,option in enumerate(list_menu):
        print(f"{index+1}.{option}")

def main():
    my_tasks = []
    while True:
        show_list()
        choice = get_choice()
        match choice:

            case '1':
                if not my_tasks: 
                    print("You have no tasks")
                for index,option in enumerate(my_tasks,start = 1):
                    print(f"{index}.{option}")

            case '2':
                task =  get_task()
                my_tasks.append(task)

            case '3':
                for index,option in enumerate(my_tasks, start = 1):
                    print(f"{index}.{option}")

                while True:
                    try:
                        task =  int(input("Enter task number you want to remove: "))
                        if task <= len(my_tasks):
                            del my_tasks[task-1]
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid task number")

            case '4':
                break

# (improvement) broken into smaller functions
"""
def show_task(my_tasks):
    if not my_tasks: 
        print("You have no tasks")
    for index,option in enumerate(my_tasks,start = 1):
        print(f"{index}.{option}")

def add_task(my_tasks):
    task =  get_task()
    my_tasks.append(task)

def dell_task(my_tasks):
    for index,option in enumerate(my_tasks, start = 1):
        print(f"{index}.{option}")
    while True:
        try:
            task =  int(input("Enter task number you want to remove: "))
            if task <= len(my_tasks):
                del my_tasks[task-1]
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid task number")

def main():
    my_tasks = []
    while True:
        show_list()
        choice = get_choice()
        match choice:
            case '1':
                show_task(my_tasks)
            case '2':
                add_task(my_tasks)
            case '3':
                dell_task(my_tasks)
            case '4':
                break
"""
def get_choice():
    while True:
        item = input(f"Enter your choice: ")
        if item in ('1','2','3','4'):
            return item
        print(f"Invalid choice")  

def get_task():
        while True:
            item = input(f"Enter your tasks: ").strip()
            if item != '':
                return item
            print(f"Invalid tasks")

"""
def checker(check):
    while True:
        item = input(f"Enter your {check}: ")

        if check == "choice": 
            if item in ('1','2','3','4'):
                return item
            print(f"Invalid {check}")  

        if check == "task":
            if item != '':
                return item
            print(f"Invalid {check}")
"""
if __name__ == '__main__':
    main()