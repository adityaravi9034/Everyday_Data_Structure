"""You are given a list of strings, where each string represents a command in a command-line interface.
The commands can be of two types: "mkdir <directory>" (creates a new directory) or "cd <directory>" 
(changes the current working directory to the specified directory). 
The directory names are alphanumeric and do not contain any spaces.

Write a function process_commands(commands) that takes the list of commands as input and returns the absolute path
of the current working directory after executing all the commands. The absolute path starts with a forward slash ("/") and includes all the 
directories from the root directory to the current working directory.

Note: The current working directory starts as the root directory ("/").
Example:
Consider the following list of commands:

commands = ["mkdir home", "cd home", "mkdir documents", "cd documents", "mkdir projects"]
The expected output for this example is "/home/documents/projects", as the commands create the "home" directory, change the current working 
directory to "home", create the "documents" directory within "home", change the current working directory to "documents", and finally create 
the "projects" directory within "documents". """


def process_commands(commands):
    current_directory = "/"
    directory_stack = []

    for command in commands:
        if command.startswith("mkdir"):
            directory_name = command.split(" ")[1]
            current_directory += directory_name + "/"
        elif command.startswith("cd"):
            directory_name = command.split(" ")[1]
            if directory_name == "..":
                if directory_stack:
                    current_directory = directory_stack.pop()
            else:
                directory_stack.append(current_directory)
                current_directory += directory_name + "/"

    return current_directory

# Example usage:
commands = ["mkdir home", "cd home", "mkdir documents", "cd documents", "mkdir projects"]
cwd = process_commands(commands)
print("Current Working Directory:", cwd)
