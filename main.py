class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"[{self.task_id}] {self.title}: {self.description}"
tasks = []
task_counter = 1  # To generate unique IDs


def create_task():
    global task_counter
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = Task(task_counter, title, description)
    tasks.append(task)
    print("✅ Task created.")
    task_counter += 1


def read_tasks():
    if not tasks:
        print("⚠️ No tasks to display.")
    else:
        print("\n📋 Task List:")
        for task in tasks:
            print(task)


def update_task():
    task_id = int(input("Enter the Task ID to update: "))
    for task in tasks:
        if task.task_id == task_id:
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            task.title = new_title
            task.description = new_description
            print("✅ Task updated.")
            return
    print("❌ Task not found.")


def delete_task():
    task_id = int(input("Enter the Task ID to delete: "))
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("✅ Task deleted.")
            return
    print("❌ Task not found.")
def main():
    while True:
        print("\n📌 Task Manager Menu")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
