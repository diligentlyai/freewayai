type Message = {
  role: string;
  content: string;
};

function convert_messages_to_format(messages: Message[], providerName: string): any {
  const validProviders = ["openai", "anthropic_messages", "anthropic_completions", "llama", "cohere"];

  if (!validProviders.includes(providerName)) {
    throw new Error(`Invalid provider name ${providerName}`);
  }

  if (providerName === "openai") {
    return messages;
  } else if (providerName === "anthropic_messages") {
    if (messages[0].role === "system") {
      return { messages: messages.slice(1), system: messages[0].content };
    } else {
      return messages;
    }
  } else if (providerName === "anthropic_completions" || providerName === "cohere") {
    const humanPrefix = providerName === "anthropic_completions" ? "\n\nHuman: " : "\nHuman: ";
    const assistantPrefix = providerName === "anthropic_completions" ? "\n\nAssistant: " : "\nAssistant: ";
    return _messages_to_string_with_prefixes(messages, humanPrefix, assistantPrefix);
  } else if (providerName === "llama") {
    const B_INST = "[INST]", E_INST = "[/INST]";
    const B_SYS = "<<SYS>>\n", E_SYS = "\n<</SYS>>\n\n";

    if (messages[0].role === "system") {
      messages[1] = { role: messages[1].role, content: B_SYS + messages[0].content + E_SYS + messages[1].content };
      messages = messages.slice(1);
    }

    messages.forEach((message, i) => {
      if (i > 0 && messages[i].role === messages[i - 1].role) {
        throw new Error("Message roles for Llama provider must alternate between user and assistant");
      }
      message.content = message.content.trim();
    });

    const humanPrefix = B_INST;
    const assistantPrefix = E_INST;
    let msg = _messages_to_string_with_prefixes(messages, humanPrefix, assistantPrefix);
    msg += E_INST;

    return msg;
  } else {
    throw new Error(`Invalid provider name ${providerName}`);
  }
}

function _messages_to_string_with_prefixes(messages: Message[], humanPrefix: string, assistantPrefix: string): string {
  let msg = "";

  messages.forEach(message => {
    if (message.role === "user") {
      msg += humanPrefix + message.content;
    } else if (message.role === "assistant") {
      msg += assistantPrefix + message.content;
    } else if (message.role === "system") {
      msg += message.content;
    } else {
      throw new Error(`Invalid message role ${message.role}`);
    }
  });

  return msg;
}

export { _messages_to_string_with_prefixes, convert_messages_to_format };