from .utilities import format_template_string, read_query_from_system_and_id

# FreewayAI is property of DiligentlyAI, Inc. and is used under an MIT license.
# by Ben Parfitt, Feb 2024

def _format_query(query, variables):
    query_template = query["search_query_template"]
    return format_template_string(query, query_template, variables)
    

def read_and_format_query(system_id, systems_location, query_id, variables):
    prompt = read_query_from_system_and_id(system_id, systems_location, query_id)
    return _format_query(prompt, variables)