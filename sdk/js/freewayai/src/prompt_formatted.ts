import { convert_messages_to_format } from './prompt_messages_to_provider_format';

type Message = {
  content: string;
  role: string;
};

class Prompt_Formatted {
  public messages: Message[];

  constructor(messages: Message[]) {
    this.messages = messages;
  }

  public toString(): string {
    if (this.messages.length === 1) {
      return this.messages[0].content;
    } else {
      return this.messages.map(message => `${message.role}: ${message.content}`).join('\n');
    }
  }

  public toList(): Message[] {
    return this.messages;
  }

  public add_context(context: string | Message[]): Prompt_Formatted {
    let newContext: Message[];

    if (typeof context === 'string') {
      newContext = [{
        content: context,
        role: 'user',
      }];
    } else if (Array.isArray(context)) {
      newContext = context;
    } else {
      throw new Error("Context must be either a string or list of message objects in OpenAI format");
    }

    if (this.messages.length === 0) {
      this.messages = newContext;
    } else if (this.messages[0].role === 'system') {
      this.messages = [...this.messages.slice(0, 1), ...newContext, ...this.messages.slice(1)];
    } else {
      this.messages = [...newContext, ...this.messages];
    }

    return this;
  }

  public to_openai(): any {
    return convert_messages_to_format(this.messages, 'openai');
  }

  public to_anthropic_messages(): any {
    return convert_messages_to_format(this.messages, 'anthropic_messages');
  }

  public to_anthropic_completions(): any {
    return convert_messages_to_format(this.messages, 'anthropic_completions');
  }

  public to_llama(): any {
    return convert_messages_to_format(this.messages, 'llama');
  }

  public to_cohere(): any {
    return convert_messages_to_format(this.messages, 'cohere');
  }
}

export { Prompt_Formatted };
