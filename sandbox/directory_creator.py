# Tool: Directory Creator

def create_directory(directory_path: str) -> None:
    
    # Creates a directory at the specified path.

    # Parameters:
    #    directory_path (str): The path where the directory will be created.

    # Returns:
    #    None

    import os

    try:
        os.makedirs(directory_path)
        print(f"Directory created at: {directory_path}")
    except FileExistsError:
        print(f"Directory already exists at: {directory_path}")
    except Exception as e:
        print(f"Error creating directory: {e}")

# Example Usage:
# Create a directory