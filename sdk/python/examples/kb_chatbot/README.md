## Example System Outline 

In this "KnowledgeBase Chatbot" example system, we are building a classic example of an LLM-backed RAG system. This is a system to answer questions about bread via an interactive commandline-based chatbot.

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
python -m chatbot
```

## Project Structure

```
system_configs/
├─ chatbot/
│  ├─ database_templates.json
│  ├─ prompt_templates.json
│  ├─ system_structure.json
│  ├─ user_inputs.json
data/
├─ bread_dataset.json
chatbot.py
sys_utilities.py
```

### Prompt Templates

The `/system_configs/chatbot` folder contains the system definitions in the format of the [FreewayAI spec](https://github.com/diligentlyai/freewayai/blob/main/docs/index.md).

### Data

This sample application has a `data/` folder with information about bread that is used to populate the in-memory vector database.

### Logging

This sample application has a utility function for calling OpenAI's API and for querying the vector database. Both of these actions result in logs being written to `chatbot_log.txt`. This can be changed or disabled, but is often useful information to have for later reflection.

