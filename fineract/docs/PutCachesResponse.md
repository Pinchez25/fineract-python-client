# PutCachesResponse

PutCachesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_type** | [**PutCachechangesSwagger**](PutCachechangesSwagger.md) |  | [optional] 

## Example

```python
from fineract_client.models.put_caches_response import PutCachesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutCachesResponse from a JSON string
put_caches_response_instance = PutCachesResponse.from_json(json)
# print the JSON string representation of the object
print PutCachesResponse.to_json()

# convert the object into a dict
put_caches_response_dict = put_caches_response_instance.to_dict()
# create an instance of PutCachesResponse from a dict
put_caches_response_form_dict = put_caches_response.from_dict(put_caches_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


