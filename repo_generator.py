import os
import sys
from distutils.dir_util import copy_tree


def change_folder_name(path_to_folder: str, new_folder_name: str):
    paths = path_to_folder.split(os.path.sep)
    paths[-1] = new_folder_name
    new_path = os.path.sep.join(paths)
    os.rename(path_to_folder, new_path)


def change_file_name(path_to_file: str, new_file_name: str):
    path, file = os.path.split(path_to_file)
    os.rename(path_to_file, os.path.join(path, new_file_name))


def replace_word_inside_file(path_to_file: str, old_word, new_word: str):
    with open(path_to_file, 'r') as f:
        text = f.read()
    text = text.replace(old_word, new_word)
    with open(path_to_file, 'w') as f:
        f.write(text)


def copy_project(path_to_project: str, destination_path: str):
    copy_tree(path_to_project, destination_path)


def need_change_inside(file_name: str):
    return (file_name.endswith('.sln') or
            file_name.endswith('.vcxproj') or
            file_name.endswith('.vcxproj.user') or
            file_name.endswith('.vcxproj.filters') or
            file_name.endswith('.gitignore') or
            file_name.endswith('.cpp') or
            file_name.endswith('.h') or
            file_name.endswith('.c') or
            file_name.endswith('.vcxproj.filters'))


def make_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def handle_file(path_to_project: str, file_name: str, old_word: str, new_word: str):
    if need_change_inside(file_name):
        replace_word_inside_file(os.path.join(path_to_project, file_name), old_word, new_word)
    if file_name.__contains__(old_word):
        change_file_name(os.path.join(path_to_project, file_name), file_name.replace(old_word, new_word))


def handle_dir(path_to_project: str, dir_name: str, old_word: str, new_word: str):
    if dir_name.__contains__(old_word):
        change_folder_name(os.path.join(path_to_project, dir_name), dir_name.replace(old_word, new_word))
        


def dirs_name_changer(path_to_project: str, old_word: str, new_word: str):
    for file in os.listdir(path_to_project):
        if os.path.isdir(os.path.join(path_to_project, file)):
            if file == '.vs' or file == 'packages':
                continue

            handle_dir(path_to_project, file, old_word, new_word)
            file = file.replace(old_word, new_word)
            dirs_name_changer(os.path.join(path_to_project, file), old_word, new_word)
        else:
            handle_file(path_to_project, file, old_word, new_word)


def change_project(path_to_project: str, destination_path: str, old_word: str, new_word: str):
    destination_path = os.path.join(destination_path, new_word)
    make_dir(destination_path)
    copy_project(path_to_project, destination_path)
    dirs_name_changer(destination_path, old_word, new_word)


if __name__ == '__main__':
    # 1: destination_folder_name
    # 2: project_name
    # 3: ??path_to_folder?? optional
    
    destination_path = sys.argv[1]
    project_name = sys.argv[2]

    if len(sys.argv) == 3:
        old_project_name = 'BaseRepo'
        path_to_folder = '.\\' + old_project_name
    else:
        path_to_folder = sys.argv[3]
        old_project_name = path_to_folder.split(os.path.sep)[-1]
        
    change_project(path_to_folder, destination_path, old_project_name, project_name)
