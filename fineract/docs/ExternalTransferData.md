# ExternalTransferData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**ExternalTransferDataDetails**](ExternalTransferDataDetails.md) |  | [optional] 
**effective_from** | **date** |  | [optional] 
**effective_to** | **date** |  | [optional] 
**loan** | [**ExternalTransferLoanData**](ExternalTransferLoanData.md) |  | [optional] 
**owner** | [**ExternalTransferOwnerData**](ExternalTransferOwnerData.md) |  | [optional] 
**purchase_price_ratio** | **str** |  | [optional] 
**settlement_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 
**sub_status** | **str** |  | [optional] 
**transfer_external_id** | **str** |  | [optional] 
**transfer_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.external_transfer_data import ExternalTransferData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTransferData from a JSON string
external_transfer_data_instance = ExternalTransferData.from_json(json)
# print the JSON string representation of the object
print(ExternalTransferData.to_json())

# convert the object into a dict
external_transfer_data_dict = external_transfer_data_instance.to_dict()
# create an instance of ExternalTransferData from a dict
external_transfer_data_from_dict = ExternalTransferData.from_dict(external_transfer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


