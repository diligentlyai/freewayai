import json

def format_messages(prompt, messages, variables):

    formatted_messages = []

    for message in messages:
        formatted_messages.append({
            "role": message["role"],
            "content": format_template_string(prompt, message["content"], variables)
        })

    return formatted_messages

def read_prompt_from_system_and_id(system_id, systems_location, prompt_id):
    with open(f'{systems_location}/{system_id}/prompt_templates.json') as f:
        prompts = json.load(f)
        target_prompt = prompts["templates"][prompt_id]
        return target_prompt
    
def read_query_from_system_and_id(system_id, systems_location, query_id):
    with open(f'{systems_location}/{system_id}/database_templates.json') as f:
        prompts = json.load(f)
        target_prompt = prompts["templates"][query_id]
        return target_prompt

def format_template_string(body, message_template, variables):
    needed_keys = [entry["name"] for entry in body["variables"]]
    for key in needed_keys:
        if key not in variables:
            raise ValueError(f"Missing required key {key}")
    
    return message_template.format(**variables)