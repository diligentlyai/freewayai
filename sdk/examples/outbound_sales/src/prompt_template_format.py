from .utilities import _read_prompt_from_system_and_id, _format_template_string
from .prompt_formatted import Prompt_Formatted

# FreewayAI is property of DiligentlyAI, Inc. and is used under an MIT license.
# by Ben Parfitt, Feb 2024

def _format_prompt(prompt, **kwargs):

    messages = []
    if "messages" in prompt:
        messages = _format_messages(prompt, prompt["messages"], **kwargs)

    if "prompt_template" in prompt:
        msg = {
            "content": _format_template_string(prompt, prompt["prompt_template"], **kwargs),
            "role": "user"
        }
        if len(messages):
            messages.append(msg)
        else:
            messages = [msg]
        
    return Prompt_Formatted(messages)

def _format_messages(prompt, messages, **kwargs):

    for message in messages:
        message["content"] = _format_template_string(prompt, message["content"], **kwargs)

    return messages

def read_and_format_prompt(system_id, systems_location, prompt_id, **kwargs):
    prompt = _read_prompt_from_system_and_id(system_id, systems_location, prompt_id)
    return _format_prompt(prompt, **kwargs)

def main():
    print(read_and_format_prompt('example', 'better_template_id', type="none here", description="none that I know of"), end="\n\n")
    print(read_and_format_prompt('example', 'better_template_id2', type="none here", description="none that I know of"), end="\n\n")
    print(read_and_format_prompt('example', 'better_template_id3', type="none here", description="none that I know of"), end="\n\n")
    print(read_and_format_prompt('example', 'better_template_id4', type="none here", description="none that I know of"), end="\n\n")

if __name__ == "__main__":
    main()