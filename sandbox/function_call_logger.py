# Tool: Function Call Logger

def function_call_logger(func):
    
    # Logs the function calls with arguments and return values.

    # Parameters:
    #    func (function): The function to be logged.

    # Returns:
    #    function: The wrapped function that logs the calls.

    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return Value: {result}")
        return result

    return wrapper

# Example Usage:
# Define a sample function
@function_call_logger
def add_numbers(a, b):
    return a + b

# Call the function
add_numbers(3, 4)