class todo_list():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
       self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            return "All tasks complete"
        return "\n".join(self.tasks)

my_todo_list = todo_list()
class todo_list():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
       self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            return "All tasks complete"
        return "\n".join(self.tasks)

my_todo_list = todo_list()

print(my_todo_list.show_tasks())