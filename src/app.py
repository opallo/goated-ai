print('importing dependencies')
import os
import json
import pprint
import loader
import prompts
import agents

print('configuring models')

with open('./config/config_list.json', 'r') as f:
  config_list = json.load(f)
  
gpt35t = config_list["config_list"][0]
gpt4 = config_list["config_list"][1]

print('creating agents')

print("Using: " + str(agents.assistant.llm_config["model"]))

# call this multiple times to register different functions to different assistants 
loader.load_and_register_functions("./config/function_registrations.json", agents.assistant, agents.user_proxy)

print('initiating chat')

result = agents.user_proxy.initiate_chat(
  agents.assistant, 
  message=prompts.prompt_better,
  summary_method="reflection_with_llm"
  )

'''print(result)'''
pprint.pprint(result.summary)
pprint.pprint(result.cost)


