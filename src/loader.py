import importlib
from autogen import register_function
from toolshed import function_registrations as fr

def load_and_register_functions(agent, user_proxy):
  
  for reg in fr.function_registrations['registrations']:
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