# GetAccountTransferTemplateResponse

GetAccountTransferTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type_options** | [**List[GetAccountOptions]**](GetAccountOptions.md) |  | [optional] 
**from_account_type_options** | [**List[GetFromAccountOptions]**](GetFromAccountOptions.md) |  | [optional] 
**to_account_type_options** | [**List[GetFromAccountOptions]**](GetFromAccountOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfer_template_response import GetAccountTransferTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransferTemplateResponse from a JSON string
get_account_transfer_template_response_instance = GetAccountTransferTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetAccountTransferTemplateResponse.to_json()

# convert the object into a dict
get_account_transfer_template_response_dict = get_account_transfer_template_response_instance.to_dict()
# create an instance of GetAccountTransferTemplateResponse from a dict
get_account_transfer_template_response_form_dict = get_account_transfer_template_response.from_dict(get_account_transfer_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


