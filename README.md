# PROJECT-1-TODO-LIST# To-Do List (Python)

DecodeLabs Python Programming, Project 1: a command-line to-do list that stores tasks in a Python list of dictionaries and saves them to a JSON file so they survive between runs.

## Features

- Add tasks to the list
- View all tasks with a done/pending marker and a summary count
- Mark a task as done
- Remove a task
- Automatic saving to `tasks.json` (persistence beyond RAM)
- Input validation for empty tasks, bad numbers and unknown choices

## Concepts Used

- Lists and `append()` for storing multiple items in one variable
- Dictionaries as task records (`id`, `task`, `done`), like a database row
- `for` loops to display tasks
- Functions that separate data logic from the user interface
- JSON serialization with the `json` module
- `if __name__ == "__main__"` entry point

## How to Run

```
python todo_list.py
```

Requires Python 3.8 or newer. No external packages needed.

## Sample Session

```
========== TO-DO LIST ==========
1. Add a task
2. View tasks
3. Mark a task as done
4. Remove a task
5. Exit

Choose an option (1-5): 2

Your Tasks
----------------------------------------
 1. [x] Finish Python assignment
 2. [ ] Buy milk
----------------------------------------
1 pending, 1 done
```
