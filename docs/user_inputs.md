

# User Inputs

<p>A list of user inputs</p>

<table>
<tbody>
<tr><th>$id</th><td>https://github.com/diligentlyai/freewayai/schema/user_inputs.json</td></tr>
<tr><th>$schema</th><td>http://json-schema.org/draft-07/schema</td></tr>
</tbody>
</table>

## Properties

<table class="jssd-properties-table"><thead><tr><th colspan="2">Name</th><th>Type</th></tr></thead><tbody><tr><td colspan="2"><a href="#_comment">_comment</a></td><td>String</td></tr><tr><td colspan="2"><a href="#inputs">inputs</a></td><td>Object</td></tr></tbody></table>



<hr />


## _comment


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">A comment to describe the user inputs for this systemn</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>




## inputs


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">A set of user inputs</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Object</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>

### Properties
  <table class="jssd-properties-table"><thead><tr><th colspan="2">Name</th><th>Type</th></tr></thead><tbody><tr><td colspan="2"><a href="#inputs<your_user_input_id>"><your_user_input_id></a></td><td>Object</td></tr></tbody></table>


### inputs.&lt;your_user_input_id&gt;


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The data about this input</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Object</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>



### inputs.&lt;your_user_input_id&gt;.input_id


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">The system-level unique id for this input</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>
    
  </tbody>
</table>




### inputs.&lt;your_user_input_id&gt;.description


<table class="jssd-property-table">
  <tbody>
    <tr>
      <th>Description</th>
      <td colspan="2">A description of the input coming through this id</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>
    
  </tbody>
</table>











<hr />

## Schema
```
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "https://github.com/diligentlyai/freewayai/schema/user_inputs.json",
    "title": "User Inputs",
    "description": "A list of user inputs",
    "type": "object",
    "properties": {
        "_comment": {
            "type": "string",
            "description": "A comment to describe the user inputs for this systemn"
        },
        "inputs": {
            "description": "A set of user inputs",
            "type": "object",
            "properties": {
                "<your_user_input_id>": {
                    "type": "object",
                    "properties": {
                        "input_id": {
                            "type": "string",
                            "description": "The system-level unique id for this input"
                        },
                        "description": {
                            "type": "string",
                            "description": "A description of the input coming through this id"
                        }
                    },
                    "required": [
                        "input_id"
                    ],
                    "description": "The data about this input"
                }
            }
        }
    }
}
```


