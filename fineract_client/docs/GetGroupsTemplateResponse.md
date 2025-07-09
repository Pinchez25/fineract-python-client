# GetGroupsTemplateResponse

GetGroupsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_options** | [**List[GetGroupsTemplateClientOptions]**](GetGroupsTemplateClientOptions.md) |  | [optional] 
**datatables** | [**List[GetGroupsTemplateDatatables]**](GetGroupsTemplateDatatables.md) |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_options** | [**List[GetGroupsTemplateOfficeOptions]**](GetGroupsTemplateOfficeOptions.md) |  | [optional] 
**staff_options** | [**List[GetGroupsTemplateStaffOptions]**](GetGroupsTemplateStaffOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_template_response import GetGroupsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsTemplateResponse from a JSON string
get_groups_template_response_instance = GetGroupsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetGroupsTemplateResponse.to_json())

# convert the object into a dict
get_groups_template_response_dict = get_groups_template_response_instance.to_dict()
# create an instance of GetGroupsTemplateResponse from a dict
get_groups_template_response_from_dict = GetGroupsTemplateResponse.from_dict(get_groups_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


