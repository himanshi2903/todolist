import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['task']} [{status}]")

def mark_completed(task_index):
    tasks = load_tasks()
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def remove_task(task_index):
    tasks = load_tasks()
    if 0 < task_index <= len(tasks):
        tasks.pop(task_index - 1)
        save_tasks(tasks)
        print("Task removed!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_index = int(input("Enter task number to mark as completed: "))
                mark_completed(task_index)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == "4":
            view_tasks()
            try:
                task_index = int(input("Enter task number to remove: "))
                remove_task(task_index)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
