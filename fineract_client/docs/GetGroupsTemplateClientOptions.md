# GetGroupsTemplateClientOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_template_client_options import GetGroupsTemplateClientOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsTemplateClientOptions from a JSON string
get_groups_template_client_options_instance = GetGroupsTemplateClientOptions.from_json(json)
# print the JSON string representation of the object
print(GetGroupsTemplateClientOptions.to_json())

# convert the object into a dict
get_groups_template_client_options_dict = get_groups_template_client_options_instance.to_dict()
# create an instance of GetGroupsTemplateClientOptions from a dict
get_groups_template_client_options_from_dict = GetGroupsTemplateClientOptions.from_dict(get_groups_template_client_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


