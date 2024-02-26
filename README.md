# FreewayAI

#### Welcome to FreewayAI: a new open-standard specification for LLM-backed systems  
Freeway is meant to provide a simple, flexible, extensible and lightweight standard for managing prompt templates, database query templates, user input points, and LLM-backed system diagrams. 

#### The units of FreewayAI  
The unit elements of Freeway are as follows:  
- Prompt Templates  
- Database Query Templates  
- User Inputs  

These units can then be used to construct a diagram of a system structure, to indicate the general flow of data.  
We know that systems built on LLMs are full of json parsing, for loops, if statements, and regexes. We just think that you should focus on outlining the LLM-specific components of a system.  
We also believe that prompt templates should be managed out of code, where they can be edited on their own lifecycle.


## Usage

There is an open source python sdk that can be installed from PyPi:

```bash
pip install freewayai
```

In the [sdk/examples/outbound_sales](https://github.com/diligentlyai/freewayai/tree/main/sdk/examples/outbound_sales) folder there is a reference implementation using the python sdk and the [FreewayAI spec](https://github.com/diligentlyai/freewayai/tree/main/sdk/examples/outbound_sales/system_configs/message_builder) to build a sample application.