# Tool: Function Registration Writer

def write_function_registrations(registrations: dict) -> None:
    
    # Writes function registrations to a file.

    # Parameters:
    #    registrations (dict): A dictionary containing function registrations.

    # Returns:
    #    None

    # Example Usage:
    # write_function_registrations(function_registrations)
    # ---

    with open("function_registrations.py", "w") as file:
        file.write("function_registrations = {\n")
        file.write("    \"registrations\": [\n")
        
        for registration in registrations["registrations"]:
            file.write("        {\n")
            file.write(f"            \"module\": \"{registration['module']}\",\n")
            file.write(f"            \"name\": \"{registration['name']}\",\n")
            file.write(f"            \"description\": \"{registration['description']}\"\n")
            file.write("        },\n")
        
        file.write("    ]\n")
        file.write("}\n")

    print("Function registrations have been written to function_registrations_output.py file.")

    # Example Usage
    # write_function_registrations(function_registrations)