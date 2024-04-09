print('importing dependencies')
import os
import pprint
import loader
import prompts.prompts as prompts
import agents.agents as agents

print('configuring models')
  
print('creating agents')

print("Using: " + str(agents.assistant.llm_config["model"]))

# call this multiple times to register different functions to different assistants 
loader.load_and_register_functions(agents.assistant, agents.user_proxy)

print('initiating chat')

result = agents.user_proxy.initiate_chat(
  agents.assistant, 
  message="Hello!",
  summary_method="reflection_with_llm"
  )

'''print(result)'''
pprint.pprint(result.summary)
pprint.pprint(result.cost)


