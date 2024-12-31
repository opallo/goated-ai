# Tool: Random Decision Maker

import random

def random_decision_maker(option1: str, option2: str) -> str:
    """
    Randomly selects between two options.

    Parameters:
        option1 (str): The first option.
        option2 (str): The second option.

    Returns:
        str: The selected option.

    Example Usage:
    random_decision_maker("Option A", "Option B")
    """
    
    selected_option = random.choice([option1, option2])
    return selected_option