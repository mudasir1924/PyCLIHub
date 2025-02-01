def task():
    """
    Task Management App: Allows users to add, update, delete, view, and exit the task manager.
    """
    tasks = []  # Empty list to store tasks
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")

    # Get the number of tasks the user wants to add initially
    total_tasks = int(input("Enter how many tasks you want to add: "))

    # Loop to get task inputs
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")  # Input task name
        tasks.append(task_name)  # Add task to list

    print(f"Today's tasks are: {tasks}")  # Display initial tasks

    # Infinite loop to continuously perform operations until the user exits
    while True:
        # Display options for task operations
        operation = int(input("Enter:\n1 - Add Task\n2 - Update Task\n3 - Delete Task\n4 - View Tasks\n5 - Exit\n"))

        if operation == 1:
            # Add a new task
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            # Update an existing task
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(updated_val)  # Find index of the task
                tasks[ind] = up  # Replace with new task
                print(f"Updated task '{updated_val}' to '{up}'")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            # Delete a task
            del_val = input("Which task do you want to delete? ")
            if del_val in tasks:
                tasks.remove(del_val)  # Remove task from list
                print(f"Task '{del_val}' has been deleted...")
            else:
                print(f"Task '{del_val}' not found.")

        elif operation == 4:
            # View all tasks
            print(f"Total tasks: {tasks}" if tasks else "No tasks available.")

        elif operation == 5:
            # Exit the program
            print("Closing the program...")
            break  # Exit the loop

        else:
            # Handle invalid input
            print("Invalid choice! Please enter a number between 1 and 5.")
        

# Call the function to start the program
task()
