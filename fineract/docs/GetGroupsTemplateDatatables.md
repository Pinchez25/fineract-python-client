# GetGroupsTemplateDatatables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_table_name** | **str** |  | [optional] 
**column_header_data** | [**List[GetGroupsTemplateColumnHeaderData]**](GetGroupsTemplateColumnHeaderData.md) |  | [optional] 
**registered_table_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_template_datatables import GetGroupsTemplateDatatables

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsTemplateDatatables from a JSON string
get_groups_template_datatables_instance = GetGroupsTemplateDatatables.from_json(json)
# print the JSON string representation of the object
print(GetGroupsTemplateDatatables.to_json())

# convert the object into a dict
get_groups_template_datatables_dict = get_groups_template_datatables_instance.to_dict()
# create an instance of GetGroupsTemplateDatatables from a dict
get_groups_template_datatables_from_dict = GetGroupsTemplateDatatables.from_dict(get_groups_template_datatables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


