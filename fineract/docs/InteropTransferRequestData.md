# InteropTransferRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**amount** | [**MoneyData**](MoneyData.md) |  | 
**expiration** | **datetime** |  | [optional] 
**expiration_local_date** | **date** |  | [optional] 
**extension_list** | [**List[ExtensionData]**](ExtensionData.md) |  | [optional] 
**fsp_commission** | [**MoneyData**](MoneyData.md) |  | [optional] 
**fsp_fee** | [**MoneyData**](MoneyData.md) |  | [optional] 
**geo_code** | [**GeoCodeData**](GeoCodeData.md) |  | [optional] 
**note** | **str** |  | [optional] 
**request_code** | **str** |  | [optional] 
**transaction_code** | **str** |  | 
**transaction_role** | **str** |  | 
**transaction_type** | [**InteropTransactionTypeData**](InteropTransactionTypeData.md) |  | [optional] 
**transfer_code** | **str** |  | 

## Example

```python
from fineract_client.models.interop_transfer_request_data import InteropTransferRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropTransferRequestData from a JSON string
interop_transfer_request_data_instance = InteropTransferRequestData.from_json(json)
# print the JSON string representation of the object
print InteropTransferRequestData.to_json()

# convert the object into a dict
interop_transfer_request_data_dict = interop_transfer_request_data_instance.to_dict()
# create an instance of InteropTransferRequestData from a dict
interop_transfer_request_data_form_dict = interop_transfer_request_data.from_dict(interop_transfer_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


