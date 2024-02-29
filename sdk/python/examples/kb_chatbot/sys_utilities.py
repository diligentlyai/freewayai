import numpy as np
from openai import OpenAI
import faiss

def open_ai_chat_call(messages, model=None, temperature=0.5):

    client = OpenAI()
    models = ["gpt-3.5-turbo-0125", "gpt-4-0125-preview"]
    if model is None:
        model = models[0]

    completion = client.chat.completions.create(
        model=model,
        messages = messages,
        temperature=temperature
    )
    
    return completion.choices[0].message.content

def open_ai_embedding_call(text, model="text-embedding-3-small"):
   
    client = OpenAI()
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model, dimensions=512).data[0].embedding

def make_faiss_index(embeddings):
    embeddings = np.array(embeddings)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def search_faiss_index(index, dataset, query, k=5):
    query_embedding = np.array([open_ai_embedding_call(query)])
    distances, indices = index.search(query_embedding, k)
    
    indices_sorted_by_distance = sorted(list(zip(distances[0], indices[0])))
    results = []
    for _, i in indices_sorted_by_distance:
        results.append(dataset[i])

    return results