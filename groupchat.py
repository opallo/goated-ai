import json
import toolshed
import pprint
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent, register_function, GroupChat

print('configuring models')

with open('./config_list.json', 'r') as f:
  config_list = json.load(f)