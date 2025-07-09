# GetAccountTransfersTemplateResponse

GetAccountTransfersTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account_type** | [**GetAccountTransfersFromAccountType**](GetAccountTransfersFromAccountType.md) |  | [optional] 
**from_account_type_options** | [**List[GetAccountTransfersFromAccountTypeOptions]**](GetAccountTransfersFromAccountTypeOptions.md) |  | [optional] 
**from_client_options** | [**List[GetAccountTransfersFromClientOptions]**](GetAccountTransfersFromClientOptions.md) |  | [optional] 
**from_office** | [**GetAccountTransfersFromOffice**](GetAccountTransfersFromOffice.md) |  | [optional] 
**from_office_options** | [**List[GetAccountTransfersFromOfficeOptions]**](GetAccountTransfersFromOfficeOptions.md) |  | [optional] 
**to_account_type_options** | [**List[GetAccountTransfersToAccountTypeOptions]**](GetAccountTransfersToAccountTypeOptions.md) |  | [optional] 
**to_office_options** | [**List[GetAccountTransfersToOfficeOptions]**](GetAccountTransfersToOfficeOptions.md) |  | [optional] 
**transfer_amount** | **int** |  | [optional] 
**transfer_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_template_response import GetAccountTransfersTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersTemplateResponse from a JSON string
get_account_transfers_template_response_instance = GetAccountTransfersTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountTransfersTemplateResponse.to_json())

# convert the object into a dict
get_account_transfers_template_response_dict = get_account_transfers_template_response_instance.to_dict()
# create an instance of GetAccountTransfersTemplateResponse from a dict
get_account_transfers_template_response_from_dict = GetAccountTransfersTemplateResponse.from_dict(get_account_transfers_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


