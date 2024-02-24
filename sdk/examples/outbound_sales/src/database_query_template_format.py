from .utilities import _format_template_string, _read_query_from_system_and_id

# FreewayAI is property of DiligentlyAI, Inc. and is used under an MIT license.
# by Ben Parfitt, Feb 2024

def _format_query(query, **kwargs):
    query_template = query["search_query_template"]
    return _format_template_string(query, query_template, **kwargs)
    

def read_and_format_query(system_id, systems_location, query_id, **kwargs):
    prompt = _read_query_from_system_and_id(system_id, systems_location, query_id)
    return _format_query(prompt, **kwargs)