# FreewayAI

## Welcome to FreewayAI: a new open-standard specification for LLM-backed systems  
Freeway is meant to provide a simple, flexible, enxtensible and lightweight standard for managing prompt templates, database query templates, user input points, and LLM-backed system diagrams. 

## The units of FreewayAI  
The unit elements of Freeway are as follows:  
- Prompt Templates  
- Database Query Templates  
- User Inputs  

These units can then be used to construct a diagram of a system structure, to indicate the general flow of data.  
We know that systems built on LLMs are full of json parsing, for loops, if statements, and regexes. We just think that you should focus on outlining the LLM-specific components of a system.

We also believe that prompt templates should be managed out of code, where they can be edited on their own lifecycle.

## Installation

```bash
pip install freewayai
```


## Usage

### Project Structure

```
system_configs/
├─ my_system/
│  ├─ database_templates.json
│  ├─ prompt_templates.json
│  ├─ system_structure.json
│  ├─ user_inputs.json
├─ my_second_system/
│  ├─ database_templates.json
│  ├─ prompt_templates.json
│  ├─ system_structure.json
│  ├─ user_inputs.json
index.py
```

### Example `prompt_templates.json` file

```json
{
  "templates": {
    "pirate_talk": {
      "prompt_id": "pirate_talk",
      "prompt_template": "Respond to this question from the user but talk like a pirate: {question}. Answer: ",
      "variables": [
        {
          "name": "question",
          "source": "user"
        }
      ]
    },
    "shakespeare_talk": {
      "prompt_id": "shakespeare_talk",
      "prompt_template": "Respond to this question from the user but talk like Shakespeare: {question}. Answer: ",
      "variables": [
        {
          "name": "question",
          "source": "user"
        }
      ]
    },
  }
}
```

### Example SDK Usage

```python
from openai import OpenAI
from freewayai import LLMSystem

SYSTEM_LOCATION = "system_configs/"

my_system = LLMSystem(SYSTEM_LOCATION, "my_system")

variables = {
  "question": input()
}

pirate_prompt = my_system.get_formatted_prompt("pirate_talk", variables)
formatted_pirate_prompt = pirate_prompt.to_openai()

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages = formatted_pirate_prompt,
    temperature=0.2
)

print(completion.choices[0].message.content)
```