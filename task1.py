class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, title):
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                break

    def mark_complete(self, title):
        for item in self.items:
            if item.title == title:
                item.completed = True
                break

    def display(self):
        for idx, item in enumerate(self.items):
            print(f"{idx+1}. [{item.completed}] {item.title}: {item.description}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List:")
        todo_list.display()

        print("\nMenu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Mark Item as Complete")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            new_item = TodoItem(title, description)
            todo_list.add_item(new_item)
        elif choice == "2":
            title = input("Enter title of item to remove: ")
            todo_list.remove_item(title)
        elif choice == "3":
            title = input("Enter title of item to mark as complete: ")
            todo_list.mark_complete(title)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
