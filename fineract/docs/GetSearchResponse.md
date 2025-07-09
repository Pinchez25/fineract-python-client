# GetSearchResponse

GetSearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_account_no** | **int** |  | [optional] 
**entity_external_id** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**entity_status** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**entity_type** | **str** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**parent_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_search_response import GetSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchResponse from a JSON string
get_search_response_instance = GetSearchResponse.from_json(json)
# print the JSON string representation of the object
print(GetSearchResponse.to_json())

# convert the object into a dict
get_search_response_dict = get_search_response_instance.to_dict()
# create an instance of GetSearchResponse from a dict
get_search_response_from_dict = GetSearchResponse.from_dict(get_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


