from .prompt_messages_to_provider_format import convert_messages_to_format

class Prompt_Formatted:
    def __init__(self, messages):
        self.messages = messages

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
    
    def add_context(self, context):

        # Check the type of context for either string or list
        if type(context) == str:
            context = [{
                "content": context,
                "role": "user"
            }]
            
        if type(context) != list:
            raise ValueError("Context must be either a string or list of message objects in OpenAI format")

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
    
