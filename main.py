import os

print("Typeshi!")

# read tasks if file exists
tasks = []
if os.path.exists("tasks.txt"):
    f = open("tasks.txt", "r")
    lines = f.readlines()
    for line in lines:
        if line != "":
            tasks.append(line.strip())
    f.close()

while True:
    command = input("Enter command (add/list/complete/edit/delete/clear/exit): ")

    if command == "add":
        task = input("Enter task: ")
        tasks.append("[ ] " + task)
        print("Task added")
        
    elif command == "list":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks")
        else:
            i = 1
            for t in tasks:
                print(str(i) + ". " + t)
                i = i + 1
        print("")

    elif command == "complete":
        id_str = input("Enter task ID to complete: ")
        id = int(id_str) - 1
        
        if id >= 0 and id < len(tasks):
            old_task = tasks[id]
            if "[ ]" in old_task:
                new_task = old_task.replace("[ ]", "[X]")
                tasks[id] = new_task
                print("Task completed")
            else:
                print("Task is already completed")
        else:
            print("Invalid ID")

    elif command == "edit":
        id_str = input("Enter task ID to edit: ")
        id = int(id_str) - 1
        
        if id >= 0 and id < len(tasks):
            new_text = input("Enter new text: ")
            
           
            if "[X]" in tasks[id]:
                tasks[id] = "[X] " + new_text
            else:
                tasks[id] = "[ ] " + new_text
                
            print("Task edited")
        else:
            print("Invalid ID")
            
    elif command == "delete":
        id_str = input("Enter task ID to delete: ")
        id = int(id_str) - 1
        
        if id >= 0 and id < len(tasks):
            del tasks[id]
            print("Task deleted")
        else:
            print("Invalid ID")
            
    elif command == "clear":
        tasks = []
        print("All tasks cleared!")
        
    elif command == "exit":
        # save the tasks to file before quitting
        f = open("tasks.txt", "w")
        for t in tasks:
            f.write(t + "\n")
        f.close()
        
        print("Goodbye!")
        break
        
    else:
        print("Unknown command")