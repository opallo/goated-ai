def speaker_selection(
  last_speaker: autogen.Agent,
  groupchat: autogen.GroupChat
) -> Union[autogen.Agent, Literal['auto', 'manual', 'random', 'round_robin'], None]:
  """Define a customized speaker selection function.
    A recommended way is to define a transition for each speaker in the groupchat.

    Parameters:
        - last_speaker: Agent
            The last speaker in the group chat.
        - groupchat: GroupChat
            The GroupChat object
    Return:
        Return one of the following:
        1. an `Agent` class, it must be one of the agents in the group chat.
        2. a string from ['auto', 'manual', 'random', 'round_robin'] to select a default method to use.
        3. None, which indicates the chat should be terminated.
    """

  pass