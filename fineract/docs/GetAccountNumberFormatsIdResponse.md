# GetAccountNumberFormatsIdResponse

GetAccountNumberFormatsIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**id** | **int** |  | [optional] 
**prefix_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_account_number_formats_id_response import GetAccountNumberFormatsIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountNumberFormatsIdResponse from a JSON string
get_account_number_formats_id_response_instance = GetAccountNumberFormatsIdResponse.from_json(json)
# print the JSON string representation of the object
print GetAccountNumberFormatsIdResponse.to_json()

# convert the object into a dict
get_account_number_formats_id_response_dict = get_account_number_formats_id_response_instance.to_dict()
# create an instance of GetAccountNumberFormatsIdResponse from a dict
get_account_number_formats_id_response_form_dict = get_account_number_formats_id_response.from_dict(get_account_number_formats_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


