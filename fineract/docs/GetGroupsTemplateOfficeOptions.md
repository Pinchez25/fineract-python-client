# GetGroupsTemplateOfficeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_template_office_options import GetGroupsTemplateOfficeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsTemplateOfficeOptions from a JSON string
get_groups_template_office_options_instance = GetGroupsTemplateOfficeOptions.from_json(json)
# print the JSON string representation of the object
print(GetGroupsTemplateOfficeOptions.to_json())

# convert the object into a dict
get_groups_template_office_options_dict = get_groups_template_office_options_instance.to_dict()
# create an instance of GetGroupsTemplateOfficeOptions from a dict
get_groups_template_office_options_from_dict = GetGroupsTemplateOfficeOptions.from_dict(get_groups_template_office_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


