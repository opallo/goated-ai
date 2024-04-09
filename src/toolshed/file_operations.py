import os
import subprocess

def list_directory_contents(directory_path: str) -> (str):

    """
    Lists the contents of the specified directory in plain English. If the operation is successful,
    it returns a message listing all items in the directory and a success code (0). If the operation
    fails, it returns an error message in plain English and an error code.
    
    Args:
    directory_path (str): The path of the directory whose contents are to be listed.
    
    Returns:
    tuple[str, int]: A tuple containing a message and a code. The message lists the contents of
                     the directory or describes the error in plain English. The code indicates the
                     result of the operation: 0 for success, and non-zero for different types of failures.
    """
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(directory_path):
            return ("The specified path does not exist.", -1)
        elif not os.path.isdir(directory_path):
            return ("The specified path is not a directory.", -2)
        
        # List the contents of the directory
        contents = os.listdir(directory_path)
        if contents:
            # Construct a plain English message listing all items
            items_listed = ", ".join(contents)
            message = f"The directory contains the following items: {items_listed}."
        else:
            message = "The directory is empty."
        
        return (message, 0)  # Success code
    except Exception as e:
        # General catch-all for any unforeseen errors
        return (f"An unexpected error occurred: {e}", -3)

  # Example usage:
  # directory_path = "path/to/your/directory"
  # message, code = list_directory_contents(directory_path)
  # print(message)
  # if code != 0:
  #     print(f"Error code: {code}")


def create_file(file_path: str) -> int:
    """
    Creates a new file at the specified path and writes a message into it.
    
    Args:
    file_path (str): The path where the new file will be created. This includes
                     the file name and its extension.
    
    Returns:
    int: A code indicating the result of the file creation operation. 0 for success,
         and non-zero for failure (e.g., -1 for an IOError).
                     
    The function opens (or creates if it doesn't exist) the file in write mode ('w'),
    which allows us to add text to the file. If the file already exists at this path,
    its content will be erased before writing the new message.
    """
    try:
        # Open the file at `file_path` in write mode ('w'). If it doesn't exist, it'll be created.
        with open(file_path, 'w') as file:
            # Write a predefined message to the file.
            file.write("This is a newly created file.")
        return 0  # Return 0 to indicate success.
    except IOError as e:
        print(f"An error occurred: {e}")  # Optionally, log the error message.
        return -1  # Return a non-zero value to indicate failure.

  # Example usage:
  # result = create_file("path/to/your/file.txt")
  # if result == 0:
  #     print("File was created successfully.")
  # else:
  #     print("Failed to create the file.")


def open_mspaint():
    """
    Opens Microsoft Paint on a Windows system.
    
    Returns:
    tuple[str, int]: A tuple containing a message indicating the result of the operation
                     and a code (0 for success, -1 for failure).
    """
    try:
        subprocess.Popen("mspaint")
        return ("Microsoft Paint has been opened successfully.", 0)
    except Exception as e:
        return (f"Failed to open Microsoft Paint: {str(e)}", -1)

  # Example usage
  # message, code = open_mspaint()
  # print(message)
  # if code != 0:
  #     print(f"Error code: {code}")
