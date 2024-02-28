import fs from "fs";

function _read_prompt_from_system_and_id(systemId: string, systemsLocation: string, promptId: string): any {
  const filePath = `${systemsLocation}/${systemId}/prompt_templates.json`;
  const fileContent = fs.readFileSync(filePath, 'utf8');
  const prompts = JSON.parse(fileContent);
  const targetPrompt = prompts["templates"][promptId];
  return targetPrompt;
}

function _read_query_from_system_and_id(systemId: string, systemsLocation: string, queryId: string): any {
  const filePath = `${systemsLocation}/${systemId}/database_templates.json`;
  const fileContent = fs.readFileSync(filePath, 'utf8');
  const queries = JSON.parse(fileContent);
  const targetQuery = queries["templates"][queryId];
  return targetQuery;
}

function _format_template_string(body: any, messageTemplate: string, variables: Record<string, any>): string {
  const neededKeys = body["variables"].map((entry: any) => entry["name"]);
  for (const key of neededKeys) {
    if (!(key in variables)) {
      throw new Error(`Missing required key ${key}`);
    }
  }

  return messageTemplate.replace(/\{([^}]+)\}/g, (match, key) => {
    if (key in variables) {
      return variables[key];
    } else {
      throw new Error(`Missing value for key ${key}`);
    }
  });
}

export { 
  _read_prompt_from_system_and_id, 
  _read_query_from_system_and_id, 
  _format_template_string 
};
