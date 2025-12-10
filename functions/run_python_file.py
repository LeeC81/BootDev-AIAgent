import os
import subprocess



def run_python_file(working_directory, file_path, args=[]):
    abs_wd = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_path.startswith(abs_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    command = ["python", abs_path, *args]

    result = subprocess.run(command, cwd=abs_wd, capture_output=True, text=True, timeout=30)


    stdout_txt = result.stdout if result.stdout else ""
    stderr_txt = result.stderr if result.stderr else ""

    try:
        if stdout_txt.strip() == "" and stderr_txt.strip() == "":
            return "No output produced"
        output = []

        output.append(f"STDOUT:\n{stdout_txt}")
        output.append(f"STDERR:\n{stderr_txt}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"


