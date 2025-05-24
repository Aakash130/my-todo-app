FILEPATH = 'todos.txt'

def get_todo(filepath=FILEPATH):
    """ Read todos from file """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todo(todo_arg,filepath=FILEPATH):
    """ Write todos to file """
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todo())