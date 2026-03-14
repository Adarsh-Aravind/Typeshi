tasks = []

while True:
    command = input("Enter command (add/list/exit): ")

    if command == "add":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif command == "list":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Unknown command")