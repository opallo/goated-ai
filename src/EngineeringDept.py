print('\nBooting AIOS 2024...\n')
print('Importing dependencies...\n')
import loader
import prompts.prompts as prompts
import agents.agents as agents
import autogen

# call this multiple times to register different functions to different assistants 
# loader.load_and_register_functions(agents.agent_1, agents.agent_2)
# 
# loader.load_and_register_functions(agents.agent_2)

print('Initiating OS...\n')

loader.load_and_register_functions(agents.reviewer, agents.executor) 

print("\n===================================")
print("=                                 =")
print("  ---+=== Welcome to AIOS ===+---")
print("            Engineering           ")
print("=                                 =")
print("===================================\n")

groupchat = autogen.GroupChat(
  agents=[agents.initializer, agents.coder, agents.executor, agents.reviewer],
  messages=[],
  max_round=30,
  speaker_selection_method=toolgen_state_transition,
  allow_repeat_speaker=False,
  send_introductions=True,
  enable_clear_history=True,
)

manager = autogen.GroupChatManager(
  groupchat=groupchat,
  system_message=prompts.group_chat_manager_prompt,
  human_input_mode="NEVER",
  description="A bot that manages conversations and replies in the group chat.",
  
)

result = agents.initializer.initiate_chat(
    manager, message="""1. BEFORE WE GET STARTED: Tell a short story, then we can move on to 2. 2. Topic: Hanging out. Requirement: Relax, it's the weekend!"""
)

# result = agents.agent_1.initiate_chat(
#   agents.agent_2, 
#   messages = [],
#   max_round=4,
#   summary_method="reflection_with_llm"
#   )

# '''print(result)'''

# pprint.pprint(result.chat_history)
# 
# pprint.pprint(result.summary)
# pprint.pprint(result.cost)

 