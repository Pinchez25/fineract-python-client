# GetHookTemplateResponse

GetHookTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupings** | [**List[Grouping]**](Grouping.md) |  | [optional] 
**templates** | [**List[HookTemplateData]**](HookTemplateData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_hook_template_response import GetHookTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHookTemplateResponse from a JSON string
get_hook_template_response_instance = GetHookTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetHookTemplateResponse.to_json()

# convert the object into a dict
get_hook_template_response_dict = get_hook_template_response_instance.to_dict()
# create an instance of GetHookTemplateResponse from a dict
get_hook_template_response_form_dict = get_hook_template_response.from_dict(get_hook_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


