import json, os
# FreewayAI is property of DiligentlyAI, Inc. and is used under an MIT license.
# by Ben Parfitt, Feb 2024

# Set env variable with os. 
# The expected directory structure is as follows: 
# <location of prompt systems>/<system_id>/prompt_templates.json
os.environ['PROMPT_SYSTEMS_LOCATION'] = '<location of prompt systems>'

PROMPT_SYSTEMS_LOCATION = os.environ['PROMPT_SYSTEMS_LOCATION']

def _format_prompt(prompt, **kwargs):

    messages = []
    if "messages" in prompt:
        messages = _format_messages(prompt, prompt["messages"], **kwargs)

    if "prompt_template" in prompt:
        msg = {
            "content": _format_message(prompt, prompt["prompt_template"], **kwargs),
            "role": "user"
        }
        if len(messages):
            messages.append(msg)
        else:
            return msg["content"]
        
    return messages

def _format_messages(prompt, messages, **kwargs):

    for message in messages:
        message["content"] = _format_message(prompt, message["content"], **kwargs)

    return messages

def _read_prompt_from_system_and_id(system_id, prompt_id):
    with open(f'{PROMPT_SYSTEMS_LOCATION}/{system_id}/prompt_templates.json') as f:
        prompts = json.load(f)
        target_prompt = prompts["templates"][prompt_id]
        return target_prompt

def _format_message(prompt, message_template, **kwargs):
    needed_keys = [entry["name"] for entry in prompt["variables"]]
    for key in needed_keys:
        if key not in kwargs:
            raise ValueError(f"Missing required key {key}")
    
    return message_template.format(**kwargs)

def read_and_format_prompt(system_id, prompt_id, **kwargs):
    prompt = _read_prompt_from_system_and_id(system_id, prompt_id)
    return _format_prompt(prompt, **kwargs)

def main():
    print(read_and_format_prompt('example', 'better_template_id', type="none here", description="none that I know of"), end="\n\n")
    print(read_and_format_prompt('example', 'better_template_id2', type="none here", description="none that I know of"), end="\n\n")
    print(read_and_format_prompt('example', 'better_template_id3', type="none here", description="none that I know of"), end="\n\n")
    print(read_and_format_prompt('example', 'better_template_id4', type="none here", description="none that I know of"), end="\n\n")

if __name__ == "__main__":
    main()