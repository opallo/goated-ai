print('\nBooting AIOS 2024...\n')
print('Importing dependencies...\n')
import pprint
import loader
import prompts.prompts as prompts
import agents.agents as agents

# call this multiple times to register different functions to different assistants 
loader.load_and_register_functions(agents.assistant, agents.user_proxy)

print('Initiating OS...\n')

print("\n===================================")
print("=                                 =")
print("\n  ---+=== Welcome to AIOS ===+---\n")
print("=                                 =")
print("===================================\n")

result = agents.user_proxy.initiate_chat(
  agents.assistant, 
  # message="Hello!",
  summary_method="reflection_with_llm"
  )

'''print(result)'''
pprint.pprint(result.summary)
pprint.pprint(result.cost)

