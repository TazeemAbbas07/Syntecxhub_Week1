import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error reading tasks file.")
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task = input("Enter task: ")

    if task == "":
        print("Task cannot be empty.")
        return

    due_date = input("Enter due date (optional): ")

    new_task = {
        "task": task,
        "completed": False,
        "due_date": due_date
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Done"
        else:
            status = "Pending"

        print(i, ".", task["task"])
        print("   Status:", status)

        if task["due_date"] != "":
            print("   Due Date:", task["due_date"])


def mark_done(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to mark as done: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            save_tasks(tasks)
            print("Deleted:", deleted["task"])
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()