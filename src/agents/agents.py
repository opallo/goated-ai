from autogen import AssistantAgent, UserProxyAgent, ConversableAgent, config_list_from_json
import prompts.prompts as prompts
from dotenv import load_dotenv

load_dotenv()

print('Configuring models...\n')

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

gpt35t = config_list["config_list"][0]
# gpt4 = config_list["config_list"][1]
# gpt4o = config_list["config_list"][2]

print('Creating agents...\n')

# =========== INITIALIZERS ============

initializer = UserProxyAgent(
  name="Init",
  code_execution_config={
    "use_docker":False
  }
)

# ============= PROXIES ===============

user_proxy = UserProxyAgent(
    name="user_proxy",
    llm_config=False,
    human_input_mode='ALWAYS',
    code_execution_config={
        "use_docker": False
    }
)

# ============= EXECUTORS =============

executor = UserProxyAgent(
    name="executor",
    system_message=prompts.executor_prompt,
    human_input_mode="ALWAYS",
    llm_config=gpt35t,
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": prompts.working_directory,
        "use_docker": False,
    },  
)

# ============== CODERS ================

coder = AssistantAgent(
  name="coder",
  llm_config=gpt35t,
  system_message=str(prompts.tool_coder_prompt)
)


# =============== RESEARCHERS ===================

scientist = AssistantAgent(
    name="scientist",
    llm_config=gpt35t,
    system_message=prompts.scientist_prompt,
)

reviewer = AssistantAgent(
    name="reviewer",
    system_message=prompts.reviewer_prompt,
    llm_config=gpt35t,
)

# ============== BRAINSTORMERS =================

agent_1 = ConversableAgent(
    name="agent_1",
    system_message=str(prompts.agent1_prompt),
    llm_config=gpt35t,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)

agent_2 = ConversableAgent(
    name="agent_2",
    system_message=str(prompts.agent2_prompt),
    llm_config=gpt35t,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)















# print("Using: " + str(assistant.llm_config["model"]) + "\n")

# assistant = AssistantAgent(
#     name="assistant",
#     system_message=str(prompts.aios_prompt),
#     llm_config=gpt35t,
#     code_execution_config=False,
#     function_map=None,
#     human_input_mode="TERMINATE",
# )