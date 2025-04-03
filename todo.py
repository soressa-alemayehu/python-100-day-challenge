import json
import os

todo_file = "todo.json"

def load_tasks():
    if os.path.exists(todo_file):
        with open(todo_file, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(todo_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f'Task "{task}" added.')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{idx}. [{status}] {task['task']}")

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f'Task {task_number} marked as complete.')
    else:
        print("Invalid task number.")

def remove_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task["task"]}" removed.')
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    while True:
        print("\nOptions: add, list, complete, remove, exit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        elif command == "list":
            list_tasks()
        elif command == "complete":
            try:
                task_number = int(input("Enter task number to complete: "))
                complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif command == "remove":
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Try again.")
