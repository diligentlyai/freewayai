

# Prompt Templates

<p>A list of prompt templates</p>

<table>
<tbody>
<tr><th>$id</th><td>https://github.com/diligentlyai/freewayai/schema/prompt_templates.json</td></tr>
<tr><th>$schema</th><td>http://json-schema.org/draft-07/schema</td></tr>
</tbody>
</table>

## Properties

<table class="jssd-properties-table"><thead><tr><th colspan="2">Name</th><th>Type</th></tr></thead><tbody><tr><td colspan="2"><a href="#_comment">_comment</a></td><td>String</td></tr><tr><th rowspan="3">templates</th><td rowspan="3">One of:</td><td>Object</td></tr><tr><td>Object</td></tr><tr><td>Object</td></tr></tbody></table>



<hr />


## _comment


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">An optional comment</td>
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
      <td colspan="2">The object containing all templates of this prompt system</td>
    </tr>
    <tr><tr><th rowspan="3">Type</th><td rowspan="3">One of:</td><td>Object</td></tr><tr><td>Object</td></tr><tr><td>Object</td></tr></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>

### Properties
  <table class="jssd-properties-table"><thead><tr><th colspan="2">Name</th><th>Type</th></tr></thead><tbody><tr><td colspan="2"><a href="#templates<your_prompt_template_id>"><your_prompt_template_id></a></td><td>Object</td></tr><tr><th colspan="2" rowspan="3">One of:</th><th></th></tr><tr><th></th></tr><tr><th></th></tr></tbody></table>


### templates.&lt;your_prompt_template_id&gt;


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The data about your prompt template</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Object</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>



### templates.&lt;your_prompt_template_id&gt;.prompt_id


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The unique identifier for this template</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>




### templates.&lt;your_prompt_template_id&gt;.prompt_template


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The prompt template itself, with keyword variables in curly brackets ({}). Optional, but only if messages is present.</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>




### templates.&lt;your_prompt_template_id&gt;.message


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The messages that will be formatted and sent. This is generally used for few-shot prompting. Optional, but only if prompt_template is present.</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>



### templates.&lt;your_prompt_template_id&gt;.messages.role


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The role of who sent that message (user OR assistant)</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>




### templates.&lt;your_prompt_template_id&gt;.messages.content


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The content of the message, with keyword variables in curly brackets ({}).</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>





### templates.&lt;your_prompt_template_id&gt;.variables


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The variables in your prompt template that will be replaced</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>



### templates.&lt;your_prompt_template_id&gt;.variables.name


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The name of the variable as found in the template string</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>




### templates.&lt;your_prompt_template_id&gt;.variables.source


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The expected source of the variable (llm, user, database)</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>






### templates.0


<table class="jssd-property-table">
  <tbody>
    
    
  </tbody>
</table>




### templates.1


<table class="jssd-property-table">
  <tbody>
    
    
  </tbody>
</table>




### templates.2


<table class="jssd-property-table">
  <tbody>
    
    
  </tbody>
</table>










<hr />

## Schema
```
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "https://github.com/diligentlyai/freewayai/schema/prompt_templates.json",
    "title": "Prompt Templates",
    "description": "A list of prompt templates",
    "type": "object",
    "properties": {
        "_comment": {
            "type": "string",
            "description": "An optional comment"
        },
        "templates": {
            "description": "The object containing all templates of this prompt system",
            "type": "object",
            "properties": {
                "<your_prompt_template_id>": {
                    "type": "object",
                    "properties": {
                        "prompt_id": {
                            "type": "string",
                            "description": "The unique identifier for this template"
                        },
                        "prompt_template": {
                            "type": "string",
                            "description": "The prompt template itself, with keyword variables in curly brackets ({}). Optional, but only if messages is present."
                        },
                        "messages": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "role": {
                                        "type": "string",
                                        "description": "The role of who sent that message (user OR assistant)"
                                    },
                                    "content": {
                                        "type": "string",
                                        "description": "The content of the message, with keyword variables in curly brackets ({})."
                                    }
                                }
                            },
                            "description": "The messages that will be formatted and sent. This is generally used for few-shot prompting. Optional, but only if prompt_template is present."
                        },
                        "variables": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "The name of the variable as found in the template string"
                                    },
                                    "source": {
                                        "type": "string",
                                        "description": "The expected source of the variable (llm, user, database)"
                                    }
                                }
                            },
                            "description": "The variables in your prompt template that will be replaced"
                        }
                    },
                    "description": "The data about your prompt template"
                }
            },
            "required": [
                "prompt_id"
            ],
            "oneOf": [
                {
                    "required": [
                        "prompt_template"
                    ]
                },
                {
                    "required": [
                        "messages"
                    ]
                },
                {
                    "anyOf": [
                        {
                            "required": [
                                "prompt_template"
                            ]
                        },
                        {
                            "required": [
                                "messages"
                            ]
                        }
                    ]
                }
            ]
        }
    }
}
```


