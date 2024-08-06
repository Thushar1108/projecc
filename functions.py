def get_todos(filepath="todos.txt"):
    """ reads the file from the filepath and opens access to the file"""
    with open(filepath, "r") as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """writes new data in the file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


def parse(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inches = float(part[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


if __name__ == "__main__":
    print("hello")
    print(get_todos())
