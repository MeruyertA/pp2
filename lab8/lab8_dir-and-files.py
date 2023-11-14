#1
import os

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_contents = os.listdir(path)
    return directories, files, all_contents

#2
import os

def path_access_checking(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

#3
import os

def path_exists_get_details(path):
    exists = os.path.exists(path)
    if exists:
        directory, filename = os.path.split(path)
        return exists, directory, filename
    else:
        return exists, None, None

#4
def count_file_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for _ in file)
    return line_count

#5
def write_list_file(file_path, some_list):
    with open(file_path, 'w') as file:
        for item in some_list:
            file.write(f"{item}\n")

#6
import string

def gen_files_alphabet():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            pass 

#7
def file_contents_copy(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)

#8
import os

def path_delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    else:
        return False

