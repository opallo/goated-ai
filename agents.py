from autogen import AssistantAgent, UserProxyAgent
import prompts
from config import config_list as cl

assistant = AssistantAgent(
  name="assistant",
  system_message=str(prompts.prompt_better),
  llm_config=cl[0],
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