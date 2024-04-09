from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import prompts.prompts as prompts
from dotenv import load_dotenv

load_dotenv()

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

gpt35t = config_list["config_list"][0]
gpt4 = config_list["config_list"][1]

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



# with open('./config/config_list.json', 'r') as f:
#   cl = json.load(f)