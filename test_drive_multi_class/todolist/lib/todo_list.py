class TodoList:
    def __init__(self):
        self.todolist = []
        

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todolist.append(todo)
        
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
    
        return self.todolist

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        self.completed = []
        for task in self.todolist:
            if task.mark_complete() != True:
                self.completed.append(task)
        return self.completed

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.todolist:
            task.mark_complete()
            



