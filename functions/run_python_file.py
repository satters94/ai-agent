import os
import subprocess

def run_python_file(working_directory, file_path):    
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
    
        if file_path:
                file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))  
    
        if not file_abs_path.startswith(working_dir_abs_path):  
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_abs_path):
            return f'Error: File "{file_path}" not found.'
        
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file.'

        result = subprocess.run(["python3", file_path], cwd=working_directory, timeout=30, capture_output=True, text=True)
        if not result.stdout and not result.stderr:
             return "No output produced."
        output = f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'
        if result.returncode != 0:
             output += f'\nProcess exited with code {result.returncode }'
        return output

    except Exception as e:
         return f"Error: executing Python file: {e}"