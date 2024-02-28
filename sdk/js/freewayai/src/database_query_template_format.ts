import { _format_template_string, _read_query_from_system_and_id } from './utilities';

interface Query {
  search_query_template: string;
}

function _format_qery(query: Query, variables: Record<string, any>): string {
  const queryTemplate = query.search_query_template;
  return _format_template_string(query, queryTemplate, variables);
}

function read_and_format_query(systemId: string, systemsLocation: string, queryId: string, variables: Record<string, any>): string {
  const query = _read_query_from_system_and_id(systemId, systemsLocation, queryId);
  return _format_qery(query, variables);
}

export { read_and_format_query };
