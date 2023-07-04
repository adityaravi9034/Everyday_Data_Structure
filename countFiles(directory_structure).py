"""You are given a directory structure that represents a file system. Each directory is represented by a string and is followed by a list of its subdirectories. 
The file system starts with a root directory ("/") and all directories are separated by a forward slash ("/"). You need to write a 
function that takes the directory structure  as input and returns the total number of files in the file system.

Write a function countFiles(directory_structure) that takes the directory structure as a string and returns the total number of files in the file system."""
#/
#|--- folder1
#|    |--- file1.txt
#|    |--- file2.txt
#|
#|--- folder2
#|    |--- subfolder1
#|    |    |--- file3.txt
#|    |
#|    |--- subfolder2
#|         |--- file4.txt
#|
#|--- folder3
#     |--- file5.txt

"""/, folder1, file1.txt, file2.txt, folder2, subfolder1, file3.txt, subfolder2, file4.txt, folder3, file5.txt"""


def countFiles(directory_structure):
    files = directory_structure.split(", ")
    count = 0
    
    for item in files:
        if "." in item:  # Check if the item is a file
            count += 1
    
    return count

# Example usage:
directory_structure = "/, folder1, file1.txt, file2.txt, folder2, subfolder1, file3.txt, subfolder2, file4.txt, folder3, file5.txt"
file_count = countFiles(directory_structure)
print("Total Number of Files:", file_count)
