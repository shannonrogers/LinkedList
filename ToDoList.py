from LinkedList import LinkedList, Node

class Task:
    def __init__(self, name):
        self.name = name           # Task description (string)
        self.complete = "incomplete"  # Status: "complete" or "incomplete"

class ToDoList:
    def __init__(self, list_name="My Tasks"):
        self.list_name = list_name
        self.tasks = LinkedList()
        self.current_position = -1      # Use your LinkedList to store Task objects
    
    # IMPLEMENT THESE METHODS:
    
    def add_task(self, task_name):
        """
        Add a new task to the end of the to-do list
        
        Args:
            task_name (str): Description of the task to add
        
        Example:
            todo.add_task("Buy groceries")
            todo.add_task("Finish homework")
        """
        task = Task(task_name)
        self.tasks.append(task)

    
    def complete_task(self, position): 
        """
        Mark a task as complete by position
        
        Args:
            position (int): Position of the task to mark complete (1-indexed)
        
        Returns:
            bool: True if task was found and marked complete, False otherwise
        
        Example:
            success = todo.complete_task(1)  # Complete first task
            if success:
                print("Task completed!")
        """
        if position < 1:
            print("Invalid position")
            return False  
        
        task = self.tasks.get_at_position(position-1)
        if task:
            task.complete = "complete"
            print(f"{task.name} completed")
            return True
        else: 
            print("No task found")
            return False

    
    def remove_task(self, position): 
    
        if position < 1:
            print("Invalid position")
            return False  
        
        task = self.tasks.get_at_position(position-1)
        if task is None:
            print("Task not found")
            return False
       
        if self.tasks.delete_at_position(position-1): 
            print(f"'{task.name}' removed from list")
            return True
        else:
            print("No task found")
            return False
      
    
    def view_all_tasks(self):
        """
        Display all tasks in the to-do list with their completion status
        
        Example output:
            My Tasks
            ========
            1. Buy groceries - Complete
            2. Finish homework -Incomplete
            3. Call dentist - Incomplete
        """
        print(f"======= {self.list_name} =======")
        current = self.tasks.head
        counter = 1
        while current: 
            print(f"{counter}.) {current.data.name} - {current.data.complete}")
            current = current.next
            counter += 1

def test_todo_list():
    """Test function to verify ToDoList functionality"""
    print("=== Testing To-Do List Implementation ===\n")
    
    # Create a new to-do list
    todo = ToDoList("School Tasks")
    
    # Test adding tasks
    print("1. Adding tasks...")
    todo.add_task("Study for math exam")
    todo.add_task("Write history essay")
    todo.add_task("Submit science project")
    todo.add_task("Read chapter 5")
    
    # Test viewing all tasks
    print("\n2. Viewing all tasks:")
    todo.view_all_tasks()
    
    # Test completing tasks
    print("\n3. Completing some tasks...")
    todo.complete_task(2)  # Complete second task
    todo.complete_task(4)  # Complete fourth task
    
    # Test viewing after completion
    print("\n4. Viewing tasks after completion:")
    todo.view_all_tasks()
    
    
    # Test removing tasks
    print("\n5. Removing a task...")
    todo.remove_task(3)  # Remove third task
    todo.view_all_tasks()
    
    # Test edge cases
    print("\n6. Testing edge cases...")
    print("Trying to complete task at invalid position:")
    result = todo.complete_task(10)  # Position that doesn't exist
    print(f"Result: {result}")
    
    print("Trying to remove task at invalid position:")
    result = todo.remove_task(0)  # Invalid position (should be 1-indexed)
    print(f"Result: {result}")
    
    print("\n=== Test completed! ===")

# Run the test
# test_todo_list()
test_todo_list()
