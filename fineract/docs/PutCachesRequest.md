# PutCachesRequest

PutCachesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_type** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_caches_request import PutCachesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutCachesRequest from a JSON string
put_caches_request_instance = PutCachesRequest.from_json(json)
# print the JSON string representation of the object
print PutCachesRequest.to_json()

# convert the object into a dict
put_caches_request_dict = put_caches_request_instance.to_dict()
# create an instance of PutCachesRequest from a dict
put_caches_request_form_dict = put_caches_request.from_dict(put_caches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


