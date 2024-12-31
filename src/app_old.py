print('\nBooting AIOS 2024...\n')
print('Importing dependencies...\n')
import pprint
import json
import loader
import prompts.prompts as prompts
import agents.agents as agents

# call this multiple times to register different functions to different assistants 
loader.load_and_register_functions(agents.agent_1, agents.agent_2)
# 
# loader.load_and_register_functions(agents.agent_2)

print('Initiating OS...\n')

print("\n===================================")
print("=                                 =")
print("\n  ---+=== Welcome to AIOS ===+---\n")
print("=                                 =")
print("===================================\n")



result = agents.agent_1.initiate_chat(
  agents.agent_2, 
  message="Hello! today we are going to learn some obscure lore!",
  max_turns=4,
  cache=None,
  summary_method="reflection_with_llm"
  )

'''print(result)'''

pprint.pprint(result.chat_history)
pprint.pprint(result.summary)
pprint.pprint(result.cost)

 