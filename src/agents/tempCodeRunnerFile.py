assistant = AssistantAgent(
    name="assistant",
    system_message=str(prompts.aios_prompt),
    llm_config=gpt35t,
    code_execution_config=False,
    function_map=None,
    human_input_mode="TERMINATE",
)