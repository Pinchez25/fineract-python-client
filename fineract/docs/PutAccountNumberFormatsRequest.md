# PutAccountNumberFormatsRequest

PutAccountNumberFormatsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix_type** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_account_number_formats_request import PutAccountNumberFormatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutAccountNumberFormatsRequest from a JSON string
put_account_number_formats_request_instance = PutAccountNumberFormatsRequest.from_json(json)
# print the JSON string representation of the object
print(PutAccountNumberFormatsRequest.to_json())

# convert the object into a dict
put_account_number_formats_request_dict = put_account_number_formats_request_instance.to_dict()
# create an instance of PutAccountNumberFormatsRequest from a dict
put_account_number_formats_request_from_dict = PutAccountNumberFormatsRequest.from_dict(put_account_number_formats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


