# GetAccountTransfersTemplateRefundByTransferFromAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**amt_for_transfer** | **float** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**GetAccountTransfersTemplateRefundByTransferCurrency**](GetAccountTransfersTemplateRefundByTransferCurrency.md) |  | [optional] 
**field_officer_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_template_refund_by_transfer_from_account import GetAccountTransfersTemplateRefundByTransferFromAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersTemplateRefundByTransferFromAccount from a JSON string
get_account_transfers_template_refund_by_transfer_from_account_instance = GetAccountTransfersTemplateRefundByTransferFromAccount.from_json(json)
# print the JSON string representation of the object
print(GetAccountTransfersTemplateRefundByTransferFromAccount.to_json())

# convert the object into a dict
get_account_transfers_template_refund_by_transfer_from_account_dict = get_account_transfers_template_refund_by_transfer_from_account_instance.to_dict()
# create an instance of GetAccountTransfersTemplateRefundByTransferFromAccount from a dict
get_account_transfers_template_refund_by_transfer_from_account_from_dict = GetAccountTransfersTemplateRefundByTransferFromAccount.from_dict(get_account_transfers_template_refund_by_transfer_from_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


