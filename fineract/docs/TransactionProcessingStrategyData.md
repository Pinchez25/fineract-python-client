# TransactionProcessingStrategyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.transaction_processing_strategy_data import TransactionProcessingStrategyData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionProcessingStrategyData from a JSON string
transaction_processing_strategy_data_instance = TransactionProcessingStrategyData.from_json(json)
# print the JSON string representation of the object
print TransactionProcessingStrategyData.to_json()

# convert the object into a dict
transaction_processing_strategy_data_dict = transaction_processing_strategy_data_instance.to_dict()
# create an instance of TransactionProcessingStrategyData from a dict
transaction_processing_strategy_data_form_dict = transaction_processing_strategy_data.from_dict(transaction_processing_strategy_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


