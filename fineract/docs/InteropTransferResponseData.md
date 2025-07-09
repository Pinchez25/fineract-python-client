# InteropTransferResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **Dict[str, object]** |  | [optional] 
**client_id** | **int** |  | [optional] 
**command_id** | **int** |  | [optional] 
**completed_timestamp** | **str** |  | [optional] 
**credit_bureau_report_data** | **Dict[str, object]** |  | [optional] 
**expiration** | **str** |  | [optional] 
**extension_list** | [**List[ExtensionData]**](ExtensionData.md) |  | [optional] 
**glim_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**gsim_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_identifier** | **str** |  | [optional] 
**rollback_transaction** | **bool** |  | [optional] 
**savings_id** | **int** |  | [optional] 
**state** | **str** |  | 
**sub_resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 
**transaction_code** | **str** |  | 
**transaction_id** | **str** |  | [optional] 
**transfer_code** | **str** |  | 

## Example

```python
from fineract_client.models.interop_transfer_response_data import InteropTransferResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropTransferResponseData from a JSON string
interop_transfer_response_data_instance = InteropTransferResponseData.from_json(json)
# print the JSON string representation of the object
print InteropTransferResponseData.to_json()

# convert the object into a dict
interop_transfer_response_data_dict = interop_transfer_response_data_instance.to_dict()
# create an instance of InteropTransferResponseData from a dict
interop_transfer_response_data_form_dict = interop_transfer_response_data.from_dict(interop_transfer_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


