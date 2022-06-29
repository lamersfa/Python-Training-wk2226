import datetime

# store next available to-do id
last_id = 0


class Todo:
    """Represent a to-do in a to-do list. Match against a string in searches.
    Able to be checked off if done."""

    def __init__(self, description, deadline, tags=""):
        """Initialize a to-do with description, deadline and search tags.
        Automatically set unique id and completion status."""
        self.description = description
        self.tags = tags
        self.creation_date = datetime.date.today()
        self.deadline = deadline
        global last_id
        last_id += 1
        self.id = last_id
        self.completed = False

    def match(self, filter, filter_completion):
        """Determine if this to-do matches the filter text.
        Return True if it matches, False otherwise.
        Case-sensitive, matches both text and tags.
        If filter_completion is True, only shows results which have completed=False."""
        if filter_completion:
            if self.completed:
                return False
            return filter in self.description or filter in self.tags
        return filter in self.description or filter in self.tags

    def time_match(self, date, filter_completion):
        """Determine if deadline matches the deadline. Returns True if it matches, False otherwise.
        datetime format. If filter_completion is True, only shows results which have completed=False."""
        if filter_completion:
            if self.completed:
                return False
            return date == self.deadline
        return date == self.deadline


class Todolist:
    """Represents a todolist, consisting of to-dos that can be tagged,
    modified, searched, and marked as complete."""

    def __init__(self):
        """Initializes todolist with an empty list."""
        self.todos = []

    def new_todo(self, description, date, tags=""):
        """Create a new to-do and add it to the list.
        Expected date formatting = DD/MM/YYYY."""
        deadline = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        self.todos.append(Todo(description, deadline, tags))

    def _find_todo(self, todo_id):
        for todo in self.todos:
            if str(todo.id) == str(todo_id):
                return todo
        return None

    def modify_description(self, todo_id, description):
        """Find to-do with given id, change its description to given value."""
        todo = self._find_todo(todo_id)
        if todo:
            todo.description = description
            return True
        return False

    def modify_tags(self, todo_id, tags):
        """Find to-do with given id, change its tags to given value."""
        todo = self._find_todo(todo_id)
        if todo:
            todo.tags = tags
            return True
        return False

    def modify_date(self, todo_id, date):
        """Find to-do with given id, change its deadline to given value.
        Expected date formatting = DD / MM / YYYY."""
        deadline = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        todo = self._find_todo(todo_id)
        if todo:
            todo.deadline = deadline
            return True
        return False

    def modify_completion(self, todo_id, completed):
        """Find to-do with given id, change its completion status to given value."""
        todo = self._find_todo(todo_id)
        if todo:
            todo.completed = completed
            return True
        return False

    def search_content(self, filter, filter_completion=False):
        """Search for to-dos where the content (description, tags) matches the filter string.
        If filter_completion is True, only shows results which have completed=False."""
        return [todo for todo in self.todos if todo.match(filter, filter_completion)]

    def search_date(self, date, filter_completion=False):
        """Search for to-dos where the deadline matches the input.
        If filter_completion is True, only shows results which have completed=False.
        Expected date formatting = DD/MM/YYYY."""
        deadline = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        return [todo for todo in self.todos if todo.time_match(deadline, filter_completion)]
