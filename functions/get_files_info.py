import os

def get_files_info(working_directory, directory=None):
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
    except:
        return f'Error: could not get absolute path for {working_directory}'
    if directory:
        try:
            dir_abs_path = os.path.abspath(os.path.join(working_directory, directory))
        except:
            return f'Error: could not get absolute path for {directory}'     
    if not dir_abs_path.startswith(working_dir_abs_path):  
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if len(dir_abs_path) > len(working_dir_abs_path):
        next_char = dir_abs_path[len(working_dir_abs_path)]
        if  next_char != "/" and next_char != "\\":
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory2'
    if not os.path.isdir(dir_abs_path):
        return f'Error: "{directory}" is not a directory'
    try:
        dir_contents = os.listdir(dir_abs_path)
    except:
        return f'Error: could not get contents of {directory}'
    
    return_string_list = []
    for content in dir_contents:
        content_path = os.path.join(dir_abs_path, content)
        return_string = "- "
        return_string += f'{content}: '
        try:
            return_string += f'file_size={os.path.getsize(content_path)}, '
        except:
            return f'Error: could not get file size of {content_path}'
        try:
            return_string += f'is_dir={os.path.isdir(content_path)}'
        except:
            return f'Error: coult not check if {content_path} is a directory'
        return_string_list.append(return_string)
    final_return_string = "\n".join(return_string_list)
    return final_return_string
