import copy, json
from .prompt_messages_to_provider_format import convert_messages_to_format
from .token_counting import count_messages_tokens
from .utilities import format_messages, format_template_string

class Prompt_Formatted:
    def __init__(self, template: dict, variables: dict):
        self.template = template
        self.variables = variables
        self.messages = []


        self.added_context = []
        self._format_prompt()

    def _format_prompt(self):

        messages = []
        if "messages" in self.template:
            messages = format_messages(self.template, self.template["messages"], self.variables)
        if "prompt_template" in self.template:
            msg = {
                "content": format_template_string(self.template, self.template["prompt_template"], self.variables),
                "role": "user"
            }
            
            messages.append(msg)
            
        self.messages = messages

        if len(self.added_context) > 0:
            for context in self.added_context:
                self._add_context(context)

    def __str__(self):
        if len(self.messages) == 1:
            return self.messages[0]["content"]
        else:
            result = ""
            for message in self.messages:
                result += f"{message['role']}: {message['content']}\n"
            return result
    
    def __list__(self):
        return self.messages
    
    def count_tokens(self):
        return count_messages_tokens(self.messages)
    
    def trim_tokens(self, max_tokens):
        last_count = self.count_tokens()
        while self.count_tokens() > max_tokens:
            for k, v in self.variables.items():
                
                if len(v) < 100:
                    continue
                else:
                    self.variables[k] = v[int(len(v)*0.1):]
            
            self._format_prompt()

            if self.count_tokens() == last_count:
                raise ValueError(f"Could not trim tokens further (current token count: {self.count_tokens()}; max tokens: {max_tokens})")
            last_count = self.count_tokens()

        return self

    def add_context(self, context):

        # Check the type of context for either string or list
        if type(context) == str:
            context = [{
                "content": context,
                "role": "user"
            }]
            
        if type(context) != list:
            raise ValueError("Context must be either a string or list of message objects in OpenAI format")

        self.added_context.append(context)
        return self._add_context(context)

    def _add_context(self, context):
        if len(self.messages) == 0:
            self.messages = context
        elif self.messages[0]["role"] == "system":
            self.messages = self.messages[:1] + context + self.messages[1:]
        else:
            self.messages = context + self.messages

        return self

    def to_openai(self):
        return convert_messages_to_format(self.messages, "openai")
    
    def to_anthropic_messages(self):
        return convert_messages_to_format(self.messages, "anthropic_messages")
    
    def to_anthropic_completions(self):
        return convert_messages_to_format(self.messages, "anthropic_completions")
    
    def to_llama(self):
        return convert_messages_to_format(self.messages, "llama")
    
    def to_cohere(self):    
        return convert_messages_to_format(self.messages, "cohere")
    
