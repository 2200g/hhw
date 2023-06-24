import os

def count_py_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                count += 1
    return count

directory_path = input("enter the dir: ")

file_count = count_py_files(directory_path)

print(f".py files in the dir: {file_count}")
