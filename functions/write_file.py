import os

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
    
        if file_path:
                file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))  
    
        if not file_abs_path.startswith(working_dir_abs_path):  
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_abs_path, "w") as f:
            f.write(content)

    except Exception as e:
         return f'Error: {e}'
    
    

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'