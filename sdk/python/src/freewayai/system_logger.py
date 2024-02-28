import json
from .llm_system import LLMSystem
from .prompt_template import PromptTemplate

class SystemLogger:
    def __init__(self, system : LLMSystem) -> None:
        self.system = system

    def log_llm_interaction(self, prompt=None, response=None, prompt_id:str=None, prompt_template:PromptTemplate=None, model:str=None, variables:dict=None, log_location=None):
        # Format a json body containing each added variable plus the system.system_id
        log_body = dict()
        log_body["system_id"] = self.system.system_id
        if prompt is not None:
            log_body["prompt"] = prompt
        elif prompt_template is not None:
            log_body["prompt"] = prompt_template.to_openai()
        elif prompt_id is not None and variables is not None:
            log_body["prompt"] = self.system.get_formatted_prompt(prompt_id, variables).to_openai()

        if response is not None:
            log_body["response"] = response
        if model is not None:
            log_body["model"] = model
        if variables is not None:
            log_body["variables"] = variables

        # If log_location is None, use stdout
        self._log_body(log_location, log_body)

    def _log_body(self, log_location, log_body):
        if log_location is None:
            print(json.dumps(log_body, indent=2))
        else:
            # if log_location is a string open the file and append the log_body, if it is a file pointer write to the file
            if isinstance(log_location, str):
                with open(log_location, 'a') as f:
                    f.write(json.dumps(log_body))
                    f.write("\n")
            elif hasattr(log_location, 'write'):
                log_location.write(json.dumps(log_body))
                log_location.write("\n")
            else:
                raise ValueError("log_location must be a string or a file pointer")
            
    def log_database_interaction(self, query=None, response=None, query_id:str=None, variables:dict=None, log_location=None):
        # Format a json body containing each added variable plus the system.system_id
        log_body = dict()
        log_body["system_id"] = self.system.system_id
        if query is not None:
            log_body["query"] = query
        elif query_id is not None and variables is not None:
            log_body["query"] = self.system.get_formatted_query(query_id, variables)

        if response is not None:
            log_body["response"] = response
        if variables is not None:
            log_body["variables"] = variables

        # If log_location is None, use stdout
        self._log_body(log_location, log_body)