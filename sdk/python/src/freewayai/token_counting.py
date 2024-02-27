import tiktoken


def count_messages_tokens(messages: list):
    return sum([count_message_tokens(message) for message in messages])

def count_message_tokens(message: dict):
    
    if "content" in message:
        return count_string_tokens(message["content"])
    else:
        return 0

def count_string_tokens(message: str):
    
    model = "gpt-4"

    encoding = tiktoken.encoding_for_model(model)
    token_count = 4
    token_count += len(encoding.encode(message))
    return int(token_count)