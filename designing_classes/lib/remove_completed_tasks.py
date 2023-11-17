class RemoveCompleted:
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        self.task_list.append(task)
        return self.task_list

    def get_task_list(self):
        if self.task_list == []:
            self.task_list.append(None)
        return f"Task List: {self.task_list}"
    
    def complete_task(self, task):
        if task in self.task_list:
            self.task_list.remove(task)
        else:
            raise Exception("Item not in List!")
        return f"Task List: {self.task_list}"
