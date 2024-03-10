import { _read_prompt_from_system_and_id, _format_template_string} from './utilities';
import { Prompt_Formatted } from './prompt_formatted';

function _format_prompt(prompt: any, variables: Record<string, any>): Prompt_Formatted {

  let messages: any[] = [];
  if (prompt.messages) {
    messages = _format_messages(prompt, prompt.messages, variables);
  }

  if (prompt.prompt_template) {
    const msg = {
      content: _format_template_string(prompt, prompt.prompt_template, variables),
      role: "user",
    };

    if (messages.length) {
      messages.push(msg);
    } else {
      messages = [msg];
    }
  }

  return new Prompt_Formatted(messages);
}

function _format_messages(prompt: any, messages: any[], variables: Record<string, any>): any[] {
  return messages.map(message => ({
    ...message,
    content: _format_template_string(prompt, message.content, variables),
  }));
}

function read_and_format_prompt(systemId: string, systemsLocation: string, promptId: string, variables: Record<string, any>): Prompt_Formatted {
  const prompt = _read_prompt_from_system_and_id(systemId, systemsLocation, promptId);

  return _format_prompt(prompt, variables);
}

export { read_and_format_prompt }

