

# Prompt Templates

<p>A list of prompt templates</p>

<table>
<tbody>
<tr><th>$id</th><td>https://github.com/diligentlyai/freewayai/schema/database_templates.json</td></tr>
<tr><th>$schema</th><td>http://json-schema.org/draft-07/schema</td></tr>
</tbody>
</table>

## Properties

<table class="jssd-properties-table"><thead><tr><th colspan="2">Name</th><th>Type</th></tr></thead><tbody><tr><td colspan="2"><a href="#_comment">_comment</a></td><td>String</td></tr><tr><td colspan="2"><a href="#templates">templates</a></td><td>Object</td></tr></tbody></table>



<hr />


## _comment


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">A comment to describe the database template</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>




## templates


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">A set of templates for the database</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Object</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>

### Properties
  <table class="jssd-properties-table"><thead><tr><th colspan="2">Name</th><th>Type</th></tr></thead><tbody><tr><td colspan="2"><a href="#templates<your_database_template_id>"><your_database_template_id></a></td><td>Object</td></tr></tbody></table>


### templates.&lt;your_database_template_id&gt;


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The data about this database template</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Object</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>



### templates.&lt;your_database_template_id&gt;.query_template_id


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The name of the query template. Should be unique in your system. </td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>
    
  </tbody>
</table>




### templates.&lt;your_database_template_id&gt;.search_query_template


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The template to be filled out and sent to the database, with keyword variables in curly brackets ({}).</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>




### templates.&lt;your_database_template_id&gt;.result_count


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The number of result documents requested or expected.</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Integer</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>




### templates.&lt;your_database_template_id&gt;.variables


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The variables in the template that are to be replaced by new data.</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>



### templates.&lt;your_database_template_id&gt;.variables.name


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The name of the variable as used in the template</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>




### templates.&lt;your_database_template_id&gt;.variables.source


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The expected source of the data for documentation purposes</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>












<hr />

## Schema
```
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "https://github.com/diligentlyai/freewayai/schema/database_templates.json",
    "title": "Prompt Templates",
    "description": "A list of prompt templates",
    "type": "object",
    "properties": {
        "_comment": {
            "type": "string",
            "description": "A comment to describe the database template"
        },
        "templates": {
            "description": "A set of templates for the database",
            "type": "object",
            "properties": {
                "<your_database_template_id>": {
                    "type": "object",
                    "properties": {
                        "query_template_id": {
                            "type": "string",
                            "description": "The name of the query template. Should be unique in your system. "
                        },
                        "search_query_template": {
                            "type": "string",
                            "description": "The template to be filled out and sent to the database, with keyword variables in curly brackets ({})."
                        },
                        "result_count": {
                            "type": "integer",
                            "description": "The number of result documents requested or expected."
                        },
                        "variables": {
                            "type": "array",
                            "description": "The variables in the template that are to be replaced by new data.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "The name of the variable as used in the template"
                                    },
                                    "source": {
                                        "type": "string",
                                        "description": "The expected source of the data for documentation purposes"
                                    }
                                }
                            }
                        }
                    },
                    "description": "The data about this database template",
                    "required": [
                        "query_template_id"
                    ]
                }
            }
        }
    }
}
```


