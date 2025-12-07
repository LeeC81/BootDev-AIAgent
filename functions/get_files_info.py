import os

def get_files_info(working_directory, directory="."):
    try:

        # Normalize the working_directory to an absolute path too
        working_directory = os.path.abspath(working_directory)
        # create full path by joining working_directory and directory
        full_path = os.path.abspath(os.path.join(working_directory, directory))    


        # validate full path is in the working_directory
        # (prevents "../../" escaping
        if not full_path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        # build output string
        output_str = []
        for name in sorted(os.listdir(full_path)):
            item_path = os.path.join(full_path, name)
            is_dir = os.path.isdir(item_path)

            # dirs are reported with size 0, files with their actual size
            size = 0 if is_dir else os.path.getsize(item_path)

            output_str.append(f" - {name}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(output_str)

    
    except Exception as e:
        # catch unexpected errors
        return f"Error: {e}"
