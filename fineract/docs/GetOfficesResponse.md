# GetOfficesResponse

GetOfficesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_parents** | [**List[GetOfficesResponse]**](GetOfficesResponse.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 
**opening_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_offices_response import GetOfficesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOfficesResponse from a JSON string
get_offices_response_instance = GetOfficesResponse.from_json(json)
# print the JSON string representation of the object
print(GetOfficesResponse.to_json())

# convert the object into a dict
get_offices_response_dict = get_offices_response_instance.to_dict()
# create an instance of GetOfficesResponse from a dict
get_offices_response_from_dict = GetOfficesResponse.from_dict(get_offices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


