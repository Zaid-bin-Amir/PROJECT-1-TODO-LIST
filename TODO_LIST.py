import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")

MENU = """
========== TO-DO LIST ==========
1. Add a task
2. View tasks
3. Mark a task as done
4. Remove a task
5. Exit
"""


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []
    return data if isinstance(data, list) else []


def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def next_id(tasks):
    return max((task["id"] for task in tasks), default=0) + 1


def add_task(tasks, title):
    title = title.strip()
    if not title:
        return None
    task = {"id": next_id(tasks), "task": title, "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    return None


def remove_task(tasks, task_id):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(index)
    return None


def count_pending(tasks):
    return sum(1 for task in tasks if not task["done"])


def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty. Add your first task!")
        return
    print("\nYour Tasks")
    print("-" * 40)
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"{task['id']:>2}. [{mark}] {task['task']}")
    print("-" * 40)
    pending = count_pending(tasks)
    print(f"{pending} pending, {len(tasks) - pending} done")


def ask_for_id(prompt):
    raw = input(prompt).strip()
    return int(raw) if raw.isdigit() else None


def handle_add(tasks):
    title = input("Enter the task: ")
    task = add_task(tasks, title)
    if task is None:
        print("A task cannot be empty.")
        return
    save_tasks(tasks)
    print(f"Added: {task['task']}")


def handle_complete(tasks):
    if not tasks:
        print("Nothing to complete yet.")
        return
    show_tasks(tasks)
    task = complete_task(tasks, ask_for_id("\nEnter the task number to mark as done: "))
    if task is None:
        print("No task found with that number.")
        return
    save_tasks(tasks)
    print(f"Completed: {task['task']}")


def handle_remove(tasks):
    if not tasks:
        print("Nothing to remove yet.")
        return
    show_tasks(tasks)
    task = remove_task(tasks, ask_for_id("\nEnter the task number to remove: "))
    if task is None:
        print("No task found with that number.")
        return
    save_tasks(tasks)
    print(f"Removed: {task['task']}")


def main():
    tasks = load_tasks()
    actions = {
        "1": handle_add,
        "2": show_tasks,
        "3": handle_complete,
        "4": handle_remove,
    }
    try:
        while True:
            print(MENU)
            choice = input("Choose an option (1-5): ").strip()
            if choice == "5":
                break
            action = actions.get(choice)
            if action is None:
                print("Invalid choice. Please enter a number from 1 to 5.")
                continue
            action(tasks)
    except (EOFError, KeyboardInterrupt):
        print()
    print("Goodbye! Your tasks are saved.")


if __name__ == "__main__":
    main()