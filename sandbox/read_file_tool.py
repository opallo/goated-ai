# Tool: Read File

def read_file(file_path: str) -> str:
    
    # Reads the contents of a file.

    # Parameters:
    #    file_path (str): The path to the file to be read.

    # Returns:
    #    str: The contents of the file as a string.

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File read successfully.")
            return content
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

# Example Usage:
# file_content = read_file("example.txt")