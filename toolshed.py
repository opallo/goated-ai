import os
from typing import Annotated, Literal, Optional, Dict, Any
import json
import orjson
from jsonschema import validate, ValidationError
import subprocess
from pydantic import BaseModel

# Define the type for the operator to restrict to specific arithmetic operations
Operator = Literal["+", "-", "*", "/"]

def calculator(a: int, b: int, operator: Annotated[Operator, "operator"]) -> int:
    """
    Performs a basic arithmetic operation on two integers.
    
    This function supports addition, subtraction, multiplication, and division. 
    The operation is specified by the 'operator' parameter.
    
    Args:
    a (int): The first operand in the arithmetic operation.
    b (int): The second operand in the arithmetic operation.
    operator (Annotated[Operator, "operator"]): The operation to perform. 
            It must be one of the following: "+", "-", "*", or "/". 
            The use of `Annotated` here adds metadata, which could be used by
            tools for validation or documentation.
            
    Returns:
    int: The result of the arithmetic operation. Note that division results are 
         converted to integers.
         
    Raises:
    ValueError: If an invalid operator is passed.
    
    Example:
    >>> calculator(10, 5, "+")
    15
    >>> calculator(10, 5, "/")
    2
    """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        # Convert the result to int to maintain a consistent return type
        return int(a / b)
    else:
        # Inform the user if the operator is not recognized
        raise ValueError("Invalid operator")

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

def append_to_file(file_path: str, text: str):
    """
    Appends the given text to a file specified by `file_path`. If the file doesn't exist,
    it will be created.
    
    Args:
    file_path (str): The path to the file you want to append text to. This includes
                     the file name and its extension.
    text (str): The text to append to the file.
    
    The function opens the file in append mode ('a'), which allows us to add text to
    the end of the file without removing its current content. If the file doesn't exist,
    it'll be created automatically.
    """
    with open(file_path, 'a') as file:
        file.write(text + "\n")

def list_directory_contents(directory_path: str) -> str:
    """
    Lists the contents of the specified directory, showing both files and directories.
    
    Args:
    directory_path (str): The path to the directory whose contents you want to list.
    
    This function uses the `os.listdir` method to retrieve all entries (files and
    directories) in the specified directory and then prints them one by one.
    """
    try:
        contents = os.listdir(directory_path)
        return(str(contents))
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory_path}'.")
# Function to rename a file
def rename_file(old_file_path: str, new_file_path: str):
    '''
    This function renames a file from old_file_path to new_file_path.

    Args:
        old_file_path (str): The current path of the file.
        new_file_path (str): The new path for the file.
    '''
    os.rename(old_file_path, new_file_path)

def load_schema(schema_path: str) -> Dict[str, Any]:
    """
    Load JSON schema from a file.

    :param schema_path: Path to the JSON schema file.
    :return: The loaded schema as a dictionary.
    """
    with open(schema_path, 'r') as schema_file:
        return json.load(schema_file)

def load_json_data(filename: str) -> Optional[Dict[str, Any]]:
    """
    Load JSON data from a file.

    :param filename: Path to the JSON file.
    :return: The loaded JSON data as a dictionary, or None if file not found.
    """
    try:
        with open(filename, 'rb') as file:
            return orjson.loads(file.read())
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def validate_json_data(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """
    Validate JSON data against a schema.

    :param data: JSON data to validate.
    :param schema: Schema to validate against.
    :return: True if data is valid, False otherwise.
    """
    try:
        validate(instance=data, schema=schema)
        print("JSON data is valid.")
        return True
    except ValidationError as ve:
        print("JSON validation error:", ve)
        return False

def update_json_data(filename: str, updates: Dict[str, Any], schema: Dict[str, Any]) -> None:
    """
    Update JSON data based on provided updates and save back to file.

    :param filename: Path to the JSON file to update.
    :param updates: Dictionary containing the updates.
    :param schema: Schema to validate the updated data against.
    """
    data = load_json_data(filename)
    if data and validate_json_data(data, schema):
        for key, value in updates.items():
            if key in data:
                data[key].update(value)
            else:
                data[key] = value
        
        if validate_json_data(data, schema):
            with open(filename, 'wb') as file:
                file.write(orjson.dumps(data))
            print("Updated data saved successfully.")
            
def modify_file_content(file_path: str, old_content: str, new_content: str) -> str:
    """
    Replaces part of the file's content from 'old_content' to 'new_content'.
    
    :param file_path: Path to the file to be modified.
    :param old_content: The content to be replaced.
    :param new_content: The content to replace with.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if old content is actually found
        if old_content in content:
            modified_content = content.replace(old_content, new_content)
            # Diagnostic print
            print("Content after replacement:", modified_content)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            return("File content updated successfully.")
        else:
            return(f"The content to replace was not found in {file_path}.")
    except FileNotFoundError:
        return(f"The file {file_path} was not found.")
    except IOError as e:
        return(f"An error occurred while accessing the file: {e}")

def read_file(file_path: str) -> str:
    """
    Reads the content of a specified file and prints it to the console.

    :param file_path: Path to the file to be read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return(file.read())
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

class FileContent(BaseModel):
    content: str
    error: str = ''

def read_file_content(file_path: str) -> FileContent:
    """
    Opens a file and reads its content, returning both the content and any error messages
    in a structured format using `pydantic.BaseModel`.
    
    Args:
    file_path (str): The path to the file you want to read.
    
    Returns:
    FileContent: A pydantic model containing the file's content as a string and an error message
                 if applicable.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return FileContent(content=content)
    except FileNotFoundError:
        return FileContent(error=f"The file '{file_path}' does not exist.")
    except PermissionError:
        return FileContent(error=f"Permission denied to access '{file_path}'.")
    except Exception as e:
        return FileContent(error=f"An error occurred: {str(e)}.")

class ExecutionResult(BaseModel):
    success: bool
    error: str = ''

def run_executable(file_path: str) -> ExecutionResult:
    """
    Attempts to run an executable file specified by `file_path`.

    Args:
    file_path (str): The full path to the executable file you want to run.
    
    Returns:
    ExecutionResult: A pydantic model indicating whether the execution was successful
                     and containing an error message if it was not.
    """
    try:
        subprocess.run([file_path], check=True)
        return ExecutionResult(success=True)
    except subprocess.CalledProcessError as e:
        return ExecutionResult(success=False, error=f"Execution failed: {e}")
    except FileNotFoundError:
        return ExecutionResult(success=False, error=f"The file '{file_path}' does not exist.")
    except PermissionError:
        return ExecutionResult(success=False, error="Permission denied.")
    except Exception as e:
        return ExecutionResult(success=False, error=f"An error occurred: {str(e)}.")