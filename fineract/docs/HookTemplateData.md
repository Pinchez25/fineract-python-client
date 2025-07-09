# HookTemplateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**var_schema** | [**List[Field]**](Field.md) |  | [optional] 

## Example

```python
from fineract_client.models.hook_template_data import HookTemplateData

# TODO update the JSON string below
json = "{}"
# create an instance of HookTemplateData from a JSON string
hook_template_data_instance = HookTemplateData.from_json(json)
# print the JSON string representation of the object
print HookTemplateData.to_json()

# convert the object into a dict
hook_template_data_dict = hook_template_data_instance.to_dict()
# create an instance of HookTemplateData from a dict
hook_template_data_form_dict = hook_template_data.from_dict(hook_template_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


