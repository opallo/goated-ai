import orjson
from jsonschema import validate, ValidationError
import json

# Load the schema
schema_path = 'C:/Projects/AutoGen/myapp/system/memory_schema.json'
with open(schema_path, 'r') as schema_file:
    schema = json.load(schema_file)

def load_json(filename):
    """Load JSON data from a file."""
    with open(filename, 'rb') as file:
        return orjson.loads(file.read())

def validate_json(data, schema):
    """Validate JSON data against a schema."""
    try:
        validate(instance=data, schema=schema)
        print("JSON data is valid.")
        return True
    except ValidationError as ve:
        print("JSON validation error:", ve)
        return False

def main():
    # Path to your memory.json file
    memory_file = 'C:/Projects/AutoGen/myapp/system/memory.json'
    
    # Load and validate the JSON data
    data = load_json(memory_file)
    if validate_json(data, schema):
        # Process the data or perform additional operations
        pass

if __name__ == "__main__":
    main()
