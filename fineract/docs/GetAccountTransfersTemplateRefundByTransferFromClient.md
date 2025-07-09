# GetAccountTransfersTemplateRefundByTransferFromClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**client_classification** | **object** |  | [optional] 
**client_type** | **object** |  | [optional] 
**display_name** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**gender** | **object** |  | [optional] 
**groups** | **object** |  | [optional] 
**id** | **int** |  | [optional] 
**lastname** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**status** | [**GetAccountTransfersStatus**](GetAccountTransfersStatus.md) |  | [optional] 
**timeline** | [**GetAccountTransfersTimeline**](GetAccountTransfersTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_template_refund_by_transfer_from_client import GetAccountTransfersTemplateRefundByTransferFromClient

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersTemplateRefundByTransferFromClient from a JSON string
get_account_transfers_template_refund_by_transfer_from_client_instance = GetAccountTransfersTemplateRefundByTransferFromClient.from_json(json)
# print the JSON string representation of the object
print GetAccountTransfersTemplateRefundByTransferFromClient.to_json()

# convert the object into a dict
get_account_transfers_template_refund_by_transfer_from_client_dict = get_account_transfers_template_refund_by_transfer_from_client_instance.to_dict()
# create an instance of GetAccountTransfersTemplateRefundByTransferFromClient from a dict
get_account_transfers_template_refund_by_transfer_from_client_form_dict = get_account_transfers_template_refund_by_transfer_from_client.from_dict(get_account_transfers_template_refund_by_transfer_from_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


