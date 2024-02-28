from .prompt_formatted import Prompt_Formatted
from .database_query_template_format import read_and_format_query
from .utilities import read_prompt_from_system_and_id
from .prompt_formatted import Prompt_Formatted

class LLMSystem:
    def __init__(self, system_id, systems_location=None):
        self.system_id = system_id
        self.systems_location = systems_location if systems_location is not None else "PROMPT_SYSTEMS_LOCATION"
        if self.systems_location is None:
            raise ValueError("PROMPT_SYSTEMS_LOCATION environment variable must be set or passed as initialization arg.")
        
    def get_formatted_prompt(self, prompt_id: str, variables: dict) -> Prompt_Formatted:
        prompt = read_prompt_from_system_and_id(self.system_id, self.systems_location, prompt_id)
        return Prompt_Formatted(prompt, variables)

    def get_formatted_query(self, query_id: str, variables: dict) -> str:
        return read_and_format_query(self.system_id, self.systems_location, query_id, variables)
