# InteropTransactionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **Dict[str, object]** |  | [optional] 
**client_id** | **int** |  | [optional] 
**command_id** | **int** |  | [optional] 
**credit_bureau_report_data** | **Dict[str, object]** |  | [optional] 
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
**sub_resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**transactions** | [**List[InteropTransactionData]**](InteropTransactionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.interop_transactions_data import InteropTransactionsData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropTransactionsData from a JSON string
interop_transactions_data_instance = InteropTransactionsData.from_json(json)
# print the JSON string representation of the object
print(InteropTransactionsData.to_json())

# convert the object into a dict
interop_transactions_data_dict = interop_transactions_data_instance.to_dict()
# create an instance of InteropTransactionsData from a dict
interop_transactions_data_from_dict = InteropTransactionsData.from_dict(interop_transactions_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


