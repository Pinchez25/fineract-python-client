# GetAccountTransfersTemplateRefundByTransferResponse

GetAccountTransfersTemplateRefundByTransferResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**GetAccountTransfersTemplateRefundByTransferCurrency**](GetAccountTransfersTemplateRefundByTransferCurrency.md) |  | [optional] 
**from_account** | [**GetAccountTransfersTemplateRefundByTransferFromAccount**](GetAccountTransfersTemplateRefundByTransferFromAccount.md) |  | [optional] 
**from_account_options** | [**List[GetAccountTransfersTemplateRefundByTransferFromAccountOptions]**](GetAccountTransfersTemplateRefundByTransferFromAccountOptions.md) |  | [optional] 
**from_account_type** | [**GetAccountTransfersPageItemsToAccountType**](GetAccountTransfersPageItemsToAccountType.md) |  | [optional] 
**from_account_type_options** | [**List[GetAccountTransfersFromAccountType]**](GetAccountTransfersFromAccountType.md) |  | [optional] 
**from_client** | [**GetAccountTransfersTemplateRefundByTransferFromClient**](GetAccountTransfersTemplateRefundByTransferFromClient.md) |  | [optional] 
**from_client_options** | [**List[GetAccountTransfersTemplateRefundByTransferFromClientOptions]**](GetAccountTransfersTemplateRefundByTransferFromClientOptions.md) |  | [optional] 
**from_office** | [**GetAccountTransfersTemplateRefundByTransferFromOffice**](GetAccountTransfersTemplateRefundByTransferFromOffice.md) |  | [optional] 
**from_office_options** | [**List[GetAccountTransfersTemplateRefundByTransferFromOfficeOptions]**](GetAccountTransfersTemplateRefundByTransferFromOfficeOptions.md) |  | [optional] 
**to_account** | [**GetAccountTransfersTemplateRefundByTransferToAccount**](GetAccountTransfersTemplateRefundByTransferToAccount.md) |  | [optional] 
**to_account_options** | [**List[GetAccountTransfersTemplateRefundByTransferToAccount]**](GetAccountTransfersTemplateRefundByTransferToAccount.md) |  | [optional] 
**to_account_type** | [**GetAccountTransfersFromAccountType**](GetAccountTransfersFromAccountType.md) |  | [optional] 
**to_account_type_options** | [**List[GetAccountTransfersFromAccountType]**](GetAccountTransfersFromAccountType.md) |  | [optional] 
**to_client** | [**GetAccountTransfersTemplateRefundByTransferToClient**](GetAccountTransfersTemplateRefundByTransferToClient.md) |  | [optional] 
**to_client_options** | [**List[GetAccountTransfersTemplateRefundByTransferFromClientOptions]**](GetAccountTransfersTemplateRefundByTransferFromClientOptions.md) |  | [optional] 
**to_office** | [**GetAccountTransfersTemplateRefundByTransferFromOffice**](GetAccountTransfersTemplateRefundByTransferFromOffice.md) |  | [optional] 
**to_office_options** | [**List[GetAccountTransfersTemplateRefundByTransferFromOfficeOptions]**](GetAccountTransfersTemplateRefundByTransferFromOfficeOptions.md) |  | [optional] 
**transfer_amount** | **float** |  | [optional] 
**transfer_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_template_refund_by_transfer_response import GetAccountTransfersTemplateRefundByTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersTemplateRefundByTransferResponse from a JSON string
get_account_transfers_template_refund_by_transfer_response_instance = GetAccountTransfersTemplateRefundByTransferResponse.from_json(json)
# print the JSON string representation of the object
print GetAccountTransfersTemplateRefundByTransferResponse.to_json()

# convert the object into a dict
get_account_transfers_template_refund_by_transfer_response_dict = get_account_transfers_template_refund_by_transfer_response_instance.to_dict()
# create an instance of GetAccountTransfersTemplateRefundByTransferResponse from a dict
get_account_transfers_template_refund_by_transfer_response_form_dict = get_account_transfers_template_refund_by_transfer_response.from_dict(get_account_transfers_template_refund_by_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


