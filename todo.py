
to_do = []

def add_task():
    new_task = input("What task do you want to add? ")
    to_do.append(new_task)

def remove_task():
    view_list()
    deletion = input("Which task do you want to remove? ")
    to_do.remove(deletion)

def view_list():
    for task in to_do:
        print(f"- {task}")

def menu():
    print('''
    1. Add Task
    2. Remove Task
    3. View List
    4. Exit
    ''')

def main():
    while True:
        menu()
        try:
            choice = int(input("Choose action: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                remove_task()
            elif choice == 3:
                view_list()
            elif choice == 4:
                print("Exiting list")
                break
            else: 
                print("Invalid Option.")
        except ValueError:
            print("Invalid Option")

if __name__ == "__main__":
    main()
