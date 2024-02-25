## Example System Outline  

#### This is a system to generate outbound sales emails and linkedin messages based on 
#### previous examples of outbound messages and the information about the customer.  

### TL;DR  
The data used to provide examples is found in the `profile_message_dataset` directory.  

Must run on `python3.9 - 3.11`, and `pip install -r requirements.txt`  

Must have you openai key save in environment variables.  

Run the code from the `outbound_sales` directory.  

### Details

In this "Outbound Sales" Example System, we are building a classic example of an LLM-backed RAG system. 
We use `OpenAI`'s API as our LLM and the `FAISS` library as an in-memory Vector Database. 
