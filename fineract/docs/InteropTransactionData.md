# InteropTransactionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **float** |  | 
**account_id** | **str** |  | 
**amount** | **float** |  | 
**booking_date_time** | **date** |  | 
**changes** | **Dict[str, object]** |  | [optional] 
**charge_amount** | **float** |  | [optional] 
**client_id** | **int** |  | [optional] 
**command_id** | **int** |  | [optional] 
**credit_bureau_report_data** | **Dict[str, object]** |  | [optional] 
**currency** | **str** |  | 
**glim_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**gsim_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_identifier** | **str** |  | [optional] 
**rollback_transaction** | **bool** |  | [optional] 
**saving_transaction_id** | **str** |  | 
**savings_id** | **int** |  | [optional] 
**sub_resource_external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**transaction_type** | **str** |  | 
**value_date_time** | **date** |  | 

## Example

```python
from fineract_client.models.interop_transaction_data import InteropTransactionData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropTransactionData from a JSON string
interop_transaction_data_instance = InteropTransactionData.from_json(json)
# print the JSON string representation of the object
print InteropTransactionData.to_json()

# convert the object into a dict
interop_transaction_data_dict = interop_transaction_data_instance.to_dict()
# create an instance of InteropTransactionData from a dict
interop_transaction_data_form_dict = interop_transaction_data.from_dict(interop_transaction_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


