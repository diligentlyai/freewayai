import os
# FreewayAI is property of DiligentlyAI, Inc. and is used under an MIT license.
# by Ben Parfitt, Feb 2024

# Set env variable with os. 
# The expected directory structure is as follows: 
# <location of prompt systems>/<system_id>/prompt_templates.json
os.environ['PROMPT_SYSTEMS_LOCATION'] = '<location of prompt systems>'

PROMPT_SYSTEMS_LOCATION = os.environ['PROMPT_SYSTEMS_LOCATION']