# PutTellersResponse

PutTellersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutTellersResponseChanges**](PutTellersResponseChanges.md) |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_tellers_response import PutTellersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutTellersResponse from a JSON string
put_tellers_response_instance = PutTellersResponse.from_json(json)
# print the JSON string representation of the object
print(PutTellersResponse.to_json())

# convert the object into a dict
put_tellers_response_dict = put_tellers_response_instance.to_dict()
# create an instance of PutTellersResponse from a dict
put_tellers_response_from_dict = PutTellersResponse.from_dict(put_tellers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


