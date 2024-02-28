import { read_and_format_prompt } from './prompt_template_format';
import { read_and_format_query } from './database_query_template_format';
import { Prompt_Formatted } from './prompt_formatted';

export default class LLMSystem {
  private systemId: string;
  private systemsLocation: string;

  constructor(systemId: string, systemsLocation: string | null = null) {
    this.systemId = systemId;
    this.systemsLocation = systemsLocation || process.env.PROMPT_SYSTEMS_LOCATION || '';
    if (!this.systemsLocation) {
      throw new Error("PROMPT_SYSTEMS_LOCATION environment variable must be set or passed as initialization arg.");
    }
  }

  public get_formatted_prompt(promptId: string, variables: Record<string, any>): Prompt_Formatted {
    return read_and_format_prompt(this.systemId, this.systemsLocation, promptId, variables);
  }

  public get_formatted_query(queryId: string, variables: Record<string, any>): string {
    return read_and_format_query(this.systemId, this.systemsLocation, queryId, variables);
  }
}