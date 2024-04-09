import importlib
import json
from autogen import register_function
from dotenv import load_dotenv

def load_and_register_functions(json_path, agent, user_proxy):
  with open(json_path, 'r') as file:
    config = json.load(file)
    config['config_list'][0]['api_key'] = load_dotenv('OPENAI_API_KEY')
    print(str(config))
    
  for reg in config['registrations']:
    module_name = reg['module']
    function_name = reg['name']
    description = reg['description']
    
    #Dynamically import the module and function
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)
    
    register_function(
      function,
        caller=agent,
        executor=user_proxy,
        name=function_name,
        description=description,
    )