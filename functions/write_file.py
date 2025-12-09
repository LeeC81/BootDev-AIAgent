import os


def write_file(working_directory, file_path, content):
    abs_wd = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_path.startswith(abs_wd):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        parent_dir = os.path.dirname(abs_path)

        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

        with open(abs_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{abs_path}" {len(content)} characters written'



    except Exception as e:
        return f"Error: {e}"
