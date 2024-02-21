

# System Templates

<p>A list of system templates</p>

<table>
<tbody>
<tr><th>$id</th><td>https://github.com/diligentlyai/freewayai/schema/system_templates.json</td></tr>
<tr><th>$schema</th><td>http://json-schema.org/draft-07/schema</td></tr>
</tbody>
</table>

## Properties

<table class="jssd-properties-table"><thead><tr><th colspan="2">Name</th><th>Type</th></tr></thead><tbody><tr><td colspan="2"><a href="#_comment">_comment</a></td><td>String</td></tr><tr><td colspan="2"><a href="#start_nodes">start_nodes</a></td><td>Array</td></tr><tr><td colspan="2"><a href="#terminating_nodes">terminating_nodes</a></td><td>Array</td></tr><tr><td colspan="2"><a href="#connections">connections</a></td><td>Array</td></tr></tbody></table>



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




## start_nodes


<table class="jssd-property-table">
  <tbody>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>
    <tr>
      <th>Unique Items</th>
      <td colspan="2">true</td>
    </tr><tr>
      <th>Min Items</th>
      <td colspan="2">1</td>
    </tr>
  </tbody>
</table>




## terminating_nodes


<table class="jssd-property-table">
  <tbody>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>
    <tr>
      <th>Unique Items</th>
      <td colspan="2">true</td>
    </tr><tr>
      <th>Min Items</th>
      <td colspan="2">1</td>
    </tr>
  </tbody>
</table>




## connections


<table class="jssd-property-table">
  <tbody>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>
    
  </tbody>
</table>



### connections.from


<table class="jssd-property-table">
  <tbody>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>




### connections.to


<table class="jssd-property-table">
  <tbody>
    <tr><th>Type</th><td colspan="2">Object</td></tr>
    
  </tbody>
</table>



### connections.to.id


<table class="jssd-property-table">
  <tbody>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>




### connections.to.variable


<table class="jssd-property-table">
  <tbody>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    
  </tbody>
</table>











<hr />

## Schema
```
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "https://github.com/diligentlyai/freewayai/schema/system_templates.json",
    "title": "System Templates",
    "description": "A list of system templates",
    "type": "object",
    "properties": {
        "_comment": {
            "type": "string",
            "description": "An optional comment"
        },
        "start_nodes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "minItems": 1,
            "uniqueItems": true
        },
        "terminating_nodes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "minItems": 1,
            "uniqueItems": true
        },
        "connections": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "from": {
                        "type": "string"
                    },
                    "to": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "variable": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "variable"
                        ]
                    }
                },
                "required": [
                    "from",
                    "to"
                ]
            }
        }
    },
    "required": [
        "start_nodes",
        "terminating_nodes",
        "connections"
    ]
}
```


