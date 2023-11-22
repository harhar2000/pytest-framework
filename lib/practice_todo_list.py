class ToDoList():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
       self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            return "All tasks complete"
        return "\n".join(self.tasks)

my_list = ToDoList()
my_list.add_task("Feed fish")
my_list.add_task("Walk dog")
print(my_list.show_tasks())