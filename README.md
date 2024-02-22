# FreewayAI

#### Welcome to FreewayAI: a new open-standard specification for LLM-backed systems  
Freeway is meant to provide a simple, flexible, enxtensible and lightweight standard for managing prompt templates, database query templates, user input points, and LLM-backed system diagrams. 

#### The units of FreewayAI  
The unit elements of Freeway are as follows:  
- Prompt Templates  
- Database Query Templates  
- User Inputs  

These units can then be used to construct a diagram of a system structure, to indicate the general flow of data.  
We know that systems built on LLMs are full of json parsing, for loops, if statements, and regexes. We just think that you should focus on outlining the LLM-specific components of a system.  
We also believe that prompt templates should be managed out of code, where they can be edited on their own lifecycle.


## Usage

#### The `examples` directory contains examples of how to interact with this format to get formatted prompts.

The expected directory structure is as follows:   
`<location of prompt systems>/<system_id>/prompt_templates.json`