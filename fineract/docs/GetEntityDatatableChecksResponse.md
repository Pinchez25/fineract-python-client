# GetEntityDatatableChecksResponse

GetEntityDatatableChecksResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datatable_name** | **str** |  | [optional] 
**entity** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**system_defined** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_entity_datatable_checks_response import GetEntityDatatableChecksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityDatatableChecksResponse from a JSON string
get_entity_datatable_checks_response_instance = GetEntityDatatableChecksResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntityDatatableChecksResponse.to_json())

# convert the object into a dict
get_entity_datatable_checks_response_dict = get_entity_datatable_checks_response_instance.to_dict()
# create an instance of GetEntityDatatableChecksResponse from a dict
get_entity_datatable_checks_response_from_dict = GetEntityDatatableChecksResponse.from_dict(get_entity_datatable_checks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


