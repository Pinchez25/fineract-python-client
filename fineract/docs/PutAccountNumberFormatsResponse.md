# PutAccountNumberFormatsResponse

PutAccountNumberFormatsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutAccountNumberFormatschangesSwagger**](PutAccountNumberFormatschangesSwagger.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_account_number_formats_response import PutAccountNumberFormatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutAccountNumberFormatsResponse from a JSON string
put_account_number_formats_response_instance = PutAccountNumberFormatsResponse.from_json(json)
# print the JSON string representation of the object
print(PutAccountNumberFormatsResponse.to_json())

# convert the object into a dict
put_account_number_formats_response_dict = put_account_number_formats_response_instance.to_dict()
# create an instance of PutAccountNumberFormatsResponse from a dict
put_account_number_formats_response_from_dict = PutAccountNumberFormatsResponse.from_dict(put_account_number_formats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


