from autogen import AssistantAgent, UserProxyAgent
import prompts.prompts as prompts
import json
#from config import config_list as cl

with open('./config/config_list.json', 'r') as f:
  cl = json.load(f)

gpt35t = cl["config_list"][0]
gpt4 = cl["config_list"][1]

assistant = AssistantAgent(
  name="assistant",
  system_message=str(prompts.prompt_better),
  llm_config=gpt35t,
  code_execution_config=False,
  function_map=None,
  human_input_mode="TERMINATE",
)

user_proxy = UserProxyAgent(
  name="user_proxy",
  llm_config=False,
  human_input_mode='ALWAYS',
  code_execution_config={
        "use_docker": False
    }
)