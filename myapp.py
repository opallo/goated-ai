print('importing dependencies')
import os
import json
import toolshed
import pprint
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent, register_function

print('configuring models')

with open('./config_list.json', 'r') as f:
  config_list = json.load(f)
  
gpt35t = config_list["config_list"][0]
gpt4 = config_list["config_list"][1]

with open('./agent_library.json', 'r') as f:
  agent_list = json.load(f)
  
software_dev_profile = agent_list[2]["profile"]
physicist_profile = agent_list[10]["profile"]

print('creating agents')

assistant = AssistantAgent(
  name="assistant",
  system_message= "you are a helpful assistant",
  llm_config=gpt35t,
  code_execution_config=False,
  function_map=None,
  human_input_mode="TERMINATE",
)

print("Using: " + str(assistant.llm_config["model"]))

user_proxy = UserProxyAgent(
  name="user_proxy",
  llm_config=False,
  human_input_mode='ALWAYS',
  code_execution_config={
        "use_docker": False
    }
)

register_function(
  toolshed.calculator,
    caller=assistant,  # The assistant agent can suggest calls to the calculator.
    executor=user_proxy,  # The user proxy agent can execute the calculator calls.
    name="calculator",  # By default, the function name is used as the tool name.
    description="A simple calculator",  # A description of the tool.
)
register_function(
  toolshed.create_file,
    caller=assistant,
    executor=user_proxy,
    name="create_file",
    description="A simple file creation tool",
)
register_function(
    toolshed.append_to_file,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="append_to_file",  # The name of the function as it should appear in the tool
    description="Appends specified text to a file, creating the file if it does not exist.",  # A brief description of what the function does
)
register_function(
    toolshed.list_directory_contents,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="list_directory_contents",  # The name of the function as it should appear in the tool
    description="Lists the contents of a specified directory, including both files and directories.",  # A brief description of what the function does
)
register_function(
  toolshed.rename_file,
  caller=assistant,
  executor=user_proxy,
  name="rename_file",
  description="Renames a file, given the file exists."
)

register_function(
    toolshed.load_schema,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="load_schema",  # The name of the function as it should appear in the tool
    description="Loads a JSON schema from a specified file, returning it as a dictionary for further use.",  # A brief description of what the function does
)

register_function(
    toolshed.load_json_data,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="load_json_data",  # The name of the function as it should appear in the tool
    description="Loads JSON data from a specified file, returning it as a dictionary for processing.",  # A brief description of what the function does
)

register_function(
    toolshed.validate_json_data,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="validate_json_data",  # The name of the function as it should appear in the tool
    description="Validates a given JSON data against a specified schema, ensuring it meets all the required structural and data type specifications.",  # A brief description of what the function does
)

register_function(
    toolshed.update_json_data,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="update_json_data",  # The name of the function as it should appear in the tool
    description="Updates and saves JSON data based on provided updates, validating against a schema to ensure data integrity.",  # A brief description of what the function does
)

register_function(
    toolshed.modify_file_content,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="modify_file_content",  # The name of the function as it should appear in the tool
    description="Replaces specified content in a file with new content, effectively 'backspacing' and replacing parts of the file's content.",  # A brief description of what the function does
)

register_function(
    toolshed.read_file,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function, assuming a string identifier
    executor=user_proxy,  # The execution context or proxy for user operations, assuming a string identifier
    name="read_file",  # The name of the function as it should appear in the tool
    description="Reads and prints the content of a specified file to the console."  # A brief description of what the function does
)

register_function(
    toolshed.read_file_content,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="read_file_content",  # The name of the function as it should appear in the tool
    description="Reads the content of a specified file and returns the content along with any error messages in a structured format.",  # A brief description of what the function does
)

register_function(
    toolshed.run_executable,  # Reference to the function being registered
    caller=assistant,  # The entity calling/registering the function
    executor=user_proxy,  # The execution context or proxy for user operations
    name="run_executable",  # The name of the function as it should appear in the tool
    description="Runs an executable file specified by the file path, providing success status and error messages.",  # A brief description of what the function does
)

prompt_meh = """
you are a helpful os assistant who speaks like a posh, fine gentleman butler. our root directory is "C:/Projects/AutoGen/myapp/". you have the ability to use several tools. Please help me with any task i give you. I ask that you make good use of the memory.json file at "./system/memory.json". this means propose the use of the appropriate tools every single response. ensure the schema is valid. The first thing you should do, before replying to the user, is to look through the file and refresh yourself on the details of the user. do not refer to this action in conversation, however, just greet the user and ask how you can help. DO NOT refer to placeholder details or communication preferences unsolicited. Always prefer to use modify_file_content over ammend_file or update_json_data when updating memory.
"""

prompt_better = """You are an AI assistant named Claude with the personality of a posh, refined English butler. Your role is to provide helpful and friendly assistance to the user with any tasks they request.

Key details:

The root directory for the project you are assisting with is "C:/Projects/AutoGen/myapp/".
There is a memory file at "./system/memory.json" containing important information about the user. At the start of each interaction, silently review this file to refresh your knowledge of the user, but do not mention doing this unless directly asked.
You have access to a set of tools to help complete tasks. When responding to the user, always propose using the most relevant and helpful tools for their specific request.
At the end of each interaction, update your memory.json appropriately with any key details. For example, if the user says they are enjoying a cup of coffee, by all means make a note of it.
If updating the memory file, prefer the modify_file_content tool over amend_file or update_json_data to ensure data integrity.
Generate outputs that conform to the expected data schemas for the task.
Do not proactively bring up placeholder details or the user's communication preferences from the memory file. Only discuss these if the user inquires about them.
To begin each interaction, greet the user warmly and ask how you may be of assistance today. Aim to satisfy their needs efficiently and comprehensively, while maintaining a pleasant, gentlemanly demeanor. Let me know if you need any clarification or have additional questions!"""

print('sending message')

result = user_proxy.initiate_chat(
  assistant, 
  message=prompt_better,
  summary_method="reflection_with_llm"
  )

'''print(result)'''
pprint.pprint(result.summary)
pprint.pprint(result.cost)


