tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "done": False})
    elif choice == "2":
        for i, t in enumerate(tasks):
            status = "✓" if t["done"] else "✗"
            print(f"{i+1}. {t['task']} [{status}]")
    elif choice == "3":
        task_num = int(input("Task number to mark done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
    elif choice == "4":
        break
    else:
        print("Invalid option.")
