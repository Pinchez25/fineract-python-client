# GetCodesResponse

GetCodesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**system_defined** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_codes_response import GetCodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCodesResponse from a JSON string
get_codes_response_instance = GetCodesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCodesResponse.to_json())

# convert the object into a dict
get_codes_response_dict = get_codes_response_instance.to_dict()
# create an instance of GetCodesResponse from a dict
get_codes_response_from_dict = GetCodesResponse.from_dict(get_codes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


