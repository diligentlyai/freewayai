require('dotenv').config();

import { open_ai_embedding_call, make_faiss_index, open_ai_chat_call, search_faiss_index } from './sys_utilities';
import LLMSystem from '../../freewayai/dist/index.js';

// Set the LLM System.
const llmSystem = new LLMSystem("message_builder", "system_configs/");

// Import the data files.
interface profileDataJSON { key: string; value: string; }
const new_profile: profileDataJSON[] = require('./data/new_profile_data.json');

interface profileAndMessageJSON { profile: string; message: string; }
const profiles_and_messages: profileAndMessageJSON[] = require('./data/profiles_and_messages.json');

async function get_new_message(message: string) {

    const textEmbeddings = [];
    for (const [index, entry] of profiles_and_messages.entries()) {
        const embedding = await open_ai_embedding_call(entry.message);
        textEmbeddings.push(embedding);
    }

    // Assuming make_faiss_index is a function that can take the embeddings array
    // and possibly returns a Promise or a synchronous value depending on its implementation
    const vectorDb: any = await make_faiss_index(textEmbeddings);

    // Get key profile elements.
    let extraction_prompt = await llmSystem.get_formatted_prompt("profile_extraction_prompt", { 
        raw_profile: new_profile 
    });

    extraction_prompt = extraction_prompt.to_openai();
    let extracted_profile = open_ai_chat_call(extraction_prompt.messages);

    // Get similar profiles.
    let profile_query = await llmSystem.get_formatted_query("get_similar_profile_id", { new_profile: extracted_profile })
    let similar_profiles_and_messages: any = await search_faiss_index(vectorDb, profiles_and_messages, profile_query)

    // Get similar profile messages.
    let sim_messages = similar_profiles_and_messages.map((entry: any) => entry.message);

    // Get description of how to write those messages
    let message_description_prompt = await llmSystem.get_formatted_prompt("messages_to_description_prompt", { messages: sim_messages }).to_openai();
    let message_description = open_ai_chat_call(message_description_prompt);

    // Get top 2 similar profiles paired with messages
    let top_2_sim_profiles_and_messages = similar_profiles_and_messages.slice(0, 2);

    // Get new message from top 2 similar profiles, description, and key profile elements
    // let profile1 = top_2_sim_profiles_and_messages[0]["profile"];
    // let profile2 = top_2_sim_profiles_and_messages[1]["profile"];
    // let message1 = top_2_sim_profiles_and_messages[0]["message"];
    // let message2 = top_2_sim_profiles_and_messages[1]["message"];

    // let new_message_prompt = await llmSystem.get_formatted_prompt("write_new_message_prompt", { 
    //     profile1: profile1, 
    //     profile2: profile2, 
    //     message1: message1, 
    //     message2: message2, 
    //     description: message_description, 
    //     new_profile: extracted_profile 
    // })

    // I want to add another few-shot example to the prompt as additional context (and to demo SDK functionality)
    // let added_context = [
    //     {
    //         "role": "user",
    //         "content": similar_profiles_and_messages[2]["profile"]
    //     },
    //     {
    //         "role": "assistant",
    //         "content": similar_profiles_and_messages[2]["message"]
    //     }
    // ]
    // new_message_prompt = new_message_prompt.add_context(added_context);
    // new_message_prompt = new_message_prompt.add_context("Replace 'Paddle' with 'FamilyFunLand'. ").to_openai();

    // new_message = open_ai_chat_call(new_message_prompt)

    //return new_message

    return 'A Message';
}

(async () => {
    try {
        let new_messages = await get_new_message('Bobo Rules');

        console.log('New Message: ', new_messages);
        
    } catch (error) {
        console.error("An error occurred:", error);
    }
})();