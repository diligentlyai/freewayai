import json
from freewayai import LLMSystem
from sys_utilities import open_ai_chat_call, open_ai_embedding_call, make_faiss_index, search_faiss_index


KNOWLEDGE_BASE_DATA = "data/bread_dataset.json"

def answer_query() -> str:

    # Get LLMSystem
    llm_system = LLMSystem("chatbot", "system_configs/")

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
    question = llm_system.get_formatted_prompt("clarity_check", query=query).to_openai()
    clarity = open_ai_chat_call(question, "chatbot", "clarity_check", log_location="chatbot_log.txt")

    if "clear" not in clarity.lower():
        # Get the answer to the user's question
        query += input(f"{clarity} ")

    # Check the vector database for related data
    extracted_data = get_related_data(llm_system, knowledge_base_data, vector_db, query)

    while len(extracted_data) == 0:
        # Write a follow-up question to ask
        follow_up = llm_system.get_formatted_prompt("follow_up_question", query=query).to_openai()
        follow_up = open_ai_chat_call(follow_up, "chatbot", "follow_up_question", log_location="chatbot_log.txt")
        query += input(f"{follow_up} ")

        # Check the vector database for related data
        extracted_data = get_related_data(llm_system, knowledge_base_data, vector_db, query)

    # Now that we have the extracted data, we can answer the query using the extracted data
    answer = llm_system.get_formatted_prompt("query_answer_with_info", query=query, info="; ".join(extracted_data)).to_openai()
    return open_ai_chat_call(answer, "chatbot", "query_answer_with_info", log_location="chatbot_log.txt")

def get_related_data(llm_system: LLMSystem, knowledge_base_data, vector_db, query):
    database_query = llm_system.get_formatted_query("get_related_data", query=query)
    related_data = search_faiss_index(vector_db, knowledge_base_data, database_query, \
                                      "chatbot", "get_related_data", log_location="chatbot_log.txt")

    # Check returned data for a match
    extracted_data = []
    for entry in related_data:
        to_check = entry["content"]
        
        extraction_prompt = llm_system.get_formatted_prompt("information_extraction", query=query, text=to_check).to_openai()
        extraction = open_ai_chat_call(extraction_prompt, "chatbot", "information_extraction", log_location="chatbot_log.txt")
        if "not present" in extraction.lower():
            continue
        extracted_data.append(extraction)
    return extracted_data

if __name__ == "__main__":
    print(answer_query())