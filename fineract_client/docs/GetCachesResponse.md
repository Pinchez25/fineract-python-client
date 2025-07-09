# GetCachesResponse

GetCachesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_caches_response import GetCachesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCachesResponse from a JSON string
get_caches_response_instance = GetCachesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCachesResponse.to_json())

# convert the object into a dict
get_caches_response_dict = get_caches_response_instance.to_dict()
# create an instance of GetCachesResponse from a dict
get_caches_response_from_dict = GetCachesResponse.from_dict(get_caches_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


