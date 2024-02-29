import json
from freewayai import LLMSystem, SystemLogger
from sys_utilities import open_ai_chat_call, open_ai_embedding_call, make_faiss_index, search_faiss_index


KNOWLEDGE_BASE_DATA = "data/bread_dataset.json"
LOG_LOCATION=None # Can change to filename or a file pointer

def answer_query() -> str:

    # Get LLMSystem
    llm_system = LLMSystem("chatbot", "system_configs/")
    llm_logger = SystemLogger(llm_system, LOG_LOCATION)

    # Build FAISS database from knowledge base data
    with open(KNOWLEDGE_BASE_DATA, "r") as file:
        knowledge_base_data = json.load(file)["data"]
        text_embeddings = []
        for entry in knowledge_base_data:
            text_embeddings.append(open_ai_embedding_call(entry["name"] + " " + entry["content"] ))

    vector_db = make_faiss_index(text_embeddings)

    # Get the user's question
    query = input("What is your question? ")

    # Confirm that the question is clear
    question = llm_system.get_formatted_prompt("clarity_check", dict(query=query)).to_openai()
    clarity = open_ai_chat_call(question)
    llm_logger.log_llm_interaction(prompt=question, prompt_id="clarity_check", response=clarity, model="openai.gpt-3.5-turbo-0125", variables=dict(query=query))

    if "clear" not in clarity.lower():
        # Get the answer to the user's question
        query += input(f"{clarity} ")

    # Check the vector database for related data
    extracted_data = get_related_data(llm_system, knowledge_base_data, vector_db, query)

    while len(extracted_data) == 0:
        # Write a follow-up question to ask
        follow_up = llm_system.get_formatted_prompt("follow_up_question", dict(query=query)).to_openai()
        follow_up = open_ai_chat_call(follow_up)
        llm_logger.log_llm_interaction(prompt=follow_up, prompt_id="follow_up_question", response=follow_up, model="openai.gpt-3.5-turbo-0125", variables=dict(query=query))
        query += input(f"{follow_up} ")

        # Check the vector database for related data
        extracted_data = get_related_data(llm_system, knowledge_base_data, vector_db, query)

    # Now that we have the extracted data, we can answer the query using the extracted data
    answer = llm_system.get_formatted_prompt("query_answer_with_info", dict(query=query, info="; ".join(extracted_data))).to_openai()
    final_response = open_ai_chat_call(answer)
    llm_logger.log_llm_interaction(prompt=answer, prompt_id="query_answer_with_info", response=final_response, model="openai.gpt-3.5-turbo-0125", variables=dict(query=query, info="; ".join(extracted_data)))
    return final_response

def get_related_data(llm_system: LLMSystem, knowledge_base_data, vector_db, query):
    llm_logger = SystemLogger(llm_system)
    database_query = llm_system.get_formatted_query("get_related_data", dict(query=query))
    related_data = search_faiss_index(vector_db, knowledge_base_data, database_query)
    llm_logger.log_database_interaction(query=database_query, query_id="get_related_data", response=related_data)

    # Check returned data for a match
    extracted_data = []
    for entry in related_data:
        to_check = entry["content"]
        
        extraction_prompt = llm_system.get_formatted_prompt("information_extraction", dict(query=query, text=to_check)).to_openai()
        extraction = open_ai_chat_call(extraction_prompt)
        llm_logger.log_llm_interaction(prompt=extraction_prompt, prompt_id="information_extraction", response=extraction, model="openai.gpt-3.5-turbo-0125", variables=dict(query=query, text=to_check))
        if "not present" in extraction.lower():
            continue
        extracted_data.append(extraction)
    return extracted_data

if __name__ == "__main__":
    print(answer_query())