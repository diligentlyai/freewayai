import json

def _read_prompt_from_system_and_id(system_id, systems_location, prompt_id):
    with open(f'{systems_location}/{system_id}/prompt_templates.json') as f:
        prompts = json.load(f)
        target_prompt = prompts["templates"][prompt_id]
        return target_prompt
    
def _read_query_from_system_and_id(system_id, systems_location, query_id):
    with open(f'{systems_location}/{system_id}/database_templates.json') as f:
        prompts = json.load(f)
        target_prompt = prompts["templates"][query_id]
        return target_prompt

def _format_template_string(body, message_template, **kwargs):
    needed_keys = [entry["name"] for entry in body["variables"]]
    for key in needed_keys:
        if key not in kwargs:
            raise ValueError(f"Missing required key {key}")
    
    return message_template.format(**kwargs)