import sys
from todolist import Todolist
import auth


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.todolist = Todolist()
        self.choices = {
            "1": self.show_todos,
            "2": self.search_todos,
            "3": self.add_todo,
            "4": self.modify_todo,
            "5": self.quit,
        }
        auth.authorizer.add_permission("access")

    def display_menu(self):
        print(
            """
Todo Menu

1. Show all todos
2. Search todos
3. Add todo
4. Modify Todo
5. Quit
"""
        )

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))

    def show_todos(self, todos=None):
        if not todos:
            todos = self.todolist.todos
        for todo in todos:
            print("{0}, {1}, Completed = {2} : {3}\n{4}".format(todo.id, todo.deadline, todo.completed, todo.tags, todo.description))

    def search_todos(self):
        answer = input("Do you want to search for a 'date' or for todos that match a search 'term'? ")
        if answer == 'date':
            date = input("Input the date you want to search for in DD/MM/YYYY format: ")
            comp = input("Do you want to include already completed todos? y/n: ")
            if comp == 'n' or comp == 'N':
                todos = self.todolist.search_date(date, True)
            else:
                todos = self.todolist.search_date(date, False)
            self.show_todos(todos)
        else:
            filter = input("Search for: ")
            comp = input("Do you want to include already completed todos? y/n: ")
            if comp == 'n' or comp == 'N':
                todos = self.todolist.search_content(filter, True)
            else:
                todos = self.todolist.search_content(filter, False)
            self.show_todos(todos)

    def add_todo(self):
        description = input("Enter a todo: ")
        deadline = input("Enter a deadline for your todo in DD/MM/YYYY format: ")
        self.todolist.new_todo(description, deadline)
        print("Your todo has been added")

    def modify_todo(self):
        id = input("Enter a todo ID: ")
        description = input("Enter a description: ")
        deadline = input("Enter a deadline: ")
        tags = input("Enter tags: ")
        completed = input("Enter a completion status: ")
        if description:
            self.todolist.modify_description(id, description)
        if deadline:
            self.todolist.modify_date(id, deadline)
        if tags:
            self.todolist.modify_tags(id, tags)
        if completed:
            self.todolist.modify_completion(id, completed)

    def quit(self):
        print("Thank you for using your todo list today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
