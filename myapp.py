print('importing dependencies')
import os
import json
import toolshed
import pprint
import importlib
import prompts
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent, register_function

def load_and_register_functions(json_path):
  with open(json_path, 'r') as file:
    config = json.load(file)
    
  for reg in config['registrations']:
    module_name = reg['module']
    function_name = reg['name']
    description = reg['description']
    
    #Dynamically import the module and function
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)
    
    register_function(
      function,
        caller=assistant,
        executor=user_proxy,
        name=function_name,
        description=description,
    )

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
  system_message=str(prompts.prompt_better),
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

load_and_register_functions("./function_registrations.json")

print('sending message')

result = user_proxy.initiate_chat(
  assistant, 
  message=prompt_better,
  summary_method="reflection_with_llm"
  )

'''print(result)'''
pprint.pprint(result.summary)
pprint.pprint(result.cost)


