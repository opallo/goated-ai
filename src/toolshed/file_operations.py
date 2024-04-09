def create_file(file_path: str):
    """
    Creates a new file at the specified path and writes a message into it.
    
    Args:
    file_path (str): The path where the new file will be created. This includes
                     the file name and its extension.
                     
    The function opens (or creates if it doesn't exist) the file in write mode ('w'),
    which allows us to add text to the file. If the file already exists at this path,
    its content will be erased before writing the new message.
    """
    # Open the file at `file_path` in write mode ('w'). If it doesn't exist, it'll be created.
    with open(file_path, 'w') as file:
        # Write a predefined message to the file.
        file.write()