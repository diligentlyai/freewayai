import json
from freewayai import LLMSystem
from sys_utilities import open_ai_chat_call, open_ai_embedding_call, make_faiss_index, search_faiss_index

NEW_PROFILE_LOCATION = "data/new_profile_data.json"
PROFILES_AND_MESSAGES_LOCATION = "data/profiles_and_messages.json"


def get_new_message(name: str) -> str:
    
    # Get LLMSystem
    llm_system = LLMSystem("message_builder", "system_configs/")

    # Build FAISS database from profiles and messages
    with open(PROFILES_AND_MESSAGES_LOCATION, "r") as file:
        profiles_and_messages = json.load(file)
        text_embeddings = []
        for entry in profiles_and_messages:
            text_embeddings.append(open_ai_embedding_call(entry["profile"]))

    vector_db = make_faiss_index(text_embeddings)
    
    # Get raw profile for name
    with open(NEW_PROFILE_LOCATION, "r") as file:
        new_profile = json.load(file)[name]

    # Get key profile elements
    extraction_prompt = llm_system.get_formatted_prompt("profile_extraction_prompt", dict(raw_profile=new_profile))
    extraction_prompt = extraction_prompt.to_openai()
    extracted_profile = open_ai_chat_call(extraction_prompt)


    # Get simillar profiles
    profile_query = llm_system.get_formatted_query("get_similar_profile_id", dict(new_profile=extracted_profile))
    similar_profiles_and_messages = search_faiss_index(vector_db, profiles_and_messages, profile_query)

    # Get simillar profile messages
    sim_messages = [entry["message"] for entry in similar_profiles_and_messages]

    # Get description of how to write those messages
    message_description_prompt = llm_system.get_formatted_prompt("messages_to_description_prompt", dict(messages=sim_messages)).to_openai()
    message_description = open_ai_chat_call(message_description_prompt)

    # Get top 2 simillar profiles paired with messages
    top_2_sim_profiles_and_messages = similar_profiles_and_messages[:2]

    # Get new message from top 2 simillar profiles, description, and key profile elements
    profile1 = top_2_sim_profiles_and_messages[0]["profile"]
    profile2 = top_2_sim_profiles_and_messages[1]["profile"]
    message1 = top_2_sim_profiles_and_messages[0]["message"]
    message2 = top_2_sim_profiles_and_messages[1]["message"]
    new_message_prompt = llm_system.get_formatted_prompt("write_new_message_prompt", dict(profile1=profile1, profile2=profile2, message1=message1, message2=message2, description=message_description, new_profile=extracted_profile))
    print(new_message_prompt.count_tokens())
    # I want to add another few-shot example to the prompt as additional context (and to demo SDK functionality)
    added_context = [
        {
            "role": "user",
            "content": similar_profiles_and_messages[2]["profile"]
        },
        {
            "role": "assistant",
            "content": similar_profiles_and_messages[2]["message"]
        }
    ]
    new_message_prompt = new_message_prompt.add_context(added_context)
    
    new_message_prompt = new_message_prompt.add_context("Replace 'Paddle' with 'FamilyFunLand'. ")
    
    new_message_prompt = new_message_prompt.to_openai()

    new_message = open_ai_chat_call(new_message_prompt)

    return new_message

if __name__ == "__main__":
    print(get_new_message("Michael Cox"))