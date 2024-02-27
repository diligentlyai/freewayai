
def convert_messages_to_format(messages, provider_name):
    # This function will convert the messages to the format that the provider requires.
    # The provider_name is the name of the provider that the messages are being converted to.
    # The messages are the messages that are being converted.
    # The return value is the messages in the format that the provider requires.
    
    valid_providers = ["openai", "anthropic_messages", "anthropic_completions", "llama", "cohere"]

    if provider_name not in valid_providers:
        raise ValueError(f"Invalid provider name {provider_name}")
    
    if provider_name == "openai":
        return messages
    
    elif provider_name == "anthropic_messages":
        
        if messages[0]["role"] == "system":
            return {"messages": messages[1:], "system": messages[0]["content"]}
        else:
            return messages
        
    elif provider_name == "anthropic_completions":
        human_prefix = "\n\nHuman: "
        assistant_prefix = "\n\nAssistant: "
        msg = _messages_to_string_with_prefixes(messages, human_prefix, assistant_prefix)
        
        return msg
        
    elif provider_name == "cohere":
        human_prefix = "\nHuman: "
        assistant_prefix = "\nAssistant: "
        msg = _messages_to_string_with_prefixes(messages, human_prefix, assistant_prefix)
        
        return msg
    
    elif provider_name == "llama":
        B_INST, E_INST = "[INST]", "[/INST]"
        B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

        # The message roles need to alternate between user and assistant. Optional: start with a system message.
        if messages[0]["role"] == "system":
            messages[1] = {"role": messages[1]["content"], "content": B_SYS + messages[0]["content"] + E_SYS + messages[1]["content"]}
            messages = messages[1:]
        
        if messages[0]["role"] != "user":
            raise ValueError("First message role for Llama provider must be user")
        if messages[1]["role"] != "assistant":
            raise ValueError("Second message role for Llama provider must be assistant")
        if messages[-1]["role"] != "user":
            raise ValueError("Last message role for Llama provider must be user")

        for i in range(1, len(messages)):
            if messages[i]["role"] == messages[i-1]["role"]:
                raise ValueError("Message roles for Llama provider must alternate between user and assistant")
            
        for message in messages:
            message["content"] = message["content"].strip()

        human_prefix = B_INST
        assistant_prefix = E_INST
        msg = _messages_to_string_with_prefixes(messages, human_prefix, assistant_prefix)
        msg = msg + E_INST

        return msg
    
    else:
        raise ValueError(f"Invalid provider name {provider_name}")

def _messages_to_string_with_prefixes(messages, human_prefix, assistant_prefix):
    msg = ""

    for message in messages:
        if message["role"] == "user":
            msg += human_prefix + message["content"]
        elif message["role"] == "assistant":
            msg += assistant_prefix + message["content"]
        elif message["role"] == "system":
            msg += message["content"]
        else:
            raise ValueError(f"Invalid message role {message['role']}")
        
    msg += assistant_prefix
    return msg