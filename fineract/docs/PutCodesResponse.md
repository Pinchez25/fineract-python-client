# PutCodesResponse

PutCodesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutCodesApichangesSwagger**](PutCodesApichangesSwagger.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_codes_response import PutCodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutCodesResponse from a JSON string
put_codes_response_instance = PutCodesResponse.from_json(json)
# print the JSON string representation of the object
print PutCodesResponse.to_json()

# convert the object into a dict
put_codes_response_dict = put_codes_response_instance.to_dict()
# create an instance of PutCodesResponse from a dict
put_codes_response_form_dict = put_codes_response.from_dict(put_codes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


