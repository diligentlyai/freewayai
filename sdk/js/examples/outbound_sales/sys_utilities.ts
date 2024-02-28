const OpenAIApi = require('openai');
const { IndexFlatL2 } = require('faiss-node');

const openai = new OpenAIApi({
    api_key: process.env.OPENAI_API_KEY || ''
});

async function open_ai_chat_call(messages: any, model: any = null) {
    const models = ["gpt-3.5-turbo-0125", "gpt-4-0125-preview"];
    if (!model) model = models[0];
    const response = await openai.createCompletion({
        model: model,
        messages: messages,
        temperature: 0.2,
    });

    const data: any = await response.json();
    return data.choices[0].message.content;
}

async function open_ai_embedding_call(text: string, model = "text-embedding-3-small") {
    text = text.replace("\n", " ");
    const response = await openai.embeddings.create({
        input: [text],
        model: model
    });

    const data: any = await response.data
    return data[0].embedding;
}

async function make_faiss_index(embeddings: any) {
    const index = new IndexFlatL2(embeddings[0].length);

    // Convert to an array.
    const typedEmbedding = new Float32Array(embeddings);
    index.add(typedEmbedding);
    return index;
}

async function search_faiss_index(index: any, dataset: any, query: any, k = 5) {

    // query_embedding = np.array([open_ai_embedding_call(query)])
    // distances, indices = index.search(query_embedding, k)

    // indices_sorted_by_distance = sorted(list(zip(distances[0], indices[0])))
    // results = []
    // for _, i in indices_sorted_by_distance:

    //     results.append(dataset[i])
    // return results
}

export { open_ai_embedding_call, open_ai_chat_call, make_faiss_index, search_faiss_index }