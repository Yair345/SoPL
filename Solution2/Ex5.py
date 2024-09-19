def task_manager():
    tasks = {}

    def add_task(task, status="Incomplete"):
        tasks[task] = status

    def get_tasks():
        return tasks

    def complete_task(task):
        if task in tasks.keys():
            tasks[task] = "complete"
        else:
            print(f"No task named {task} found")

    return {"add_task": add_task, "get_tasks": get_tasks, "complete_task": complete_task}


# Create a new task manager
tasks_manager = task_manager()
# Add tasks
tasks_manager['add_task']("Write email")
tasks_manager['add_task']("Shopping", "in progress")
tasks_manager['add_task']("Homework")
# Get the list of tasks
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)
# Should print: {'Write email': 'incomplete', 'Shopping': 'in progress', 'Homework':'incomplete'}
# Mark a task as complete
tasks_manager['complete_task']("Write email")
# Get the list of tasks after marking and deleting
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)
# Should print: {'Write email': 'complete', 'Shopping': 'in progress', 'Homework': 'incomplete'}



