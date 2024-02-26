## Example System Outline 

In this "Outbound Sales" example system, we are building a classic example of an LLM-backed RAG system. This is a system to generate outbound sales LinkedIn messages based on previous examples of outbound messages and the information about the customer.

We use `OpenAI`'s API as our LLM and the `FAISS` library as an in-memory Vector Database. 

## Installation

> [!IMPORTANT]
> This project only supports python 3.9-3.11

### Install python dependencies
```bash
pip install -r requirements.txt
```

### OpenAI API Key

In order to run this application you need an `OPENAI_API_KEY` environment variable.

```bash
export OPENAI_API_KEY="<your api key>"
```

## Running the Application

```bash
python -m message_builder
```

## Project Structure

```
system_configs/
├─ message_builder/
│  ├─ database_templates.json
│  ├─ prompt_templates.json
│  ├─ system_structure.json
│  ├─ user_inputs.json
data/
├─ new_profile_data.json
├─ profiles_and_messages.json
message_builder.py
sys_utilities.py
```

### Prompt Templates

The `/system_configs/message_builder` folder contains the system definitions in the format of the [FreewayAI spec](https://github.com/diligentlyai/freewayai/blob/main/docs/index.md).

### Data

This sample application has a `data/` folder with fake LinkedIn profiles which are fed as variables to the prompts, and used to populate the in-memory vector database.

