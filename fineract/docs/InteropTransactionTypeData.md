# InteropTransactionTypeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator** | **str** |  | 
**initiator_type** | **str** |  | 
**scenario** | **str** |  | 
**sub_scenario** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.interop_transaction_type_data import InteropTransactionTypeData

# TODO update the JSON string below
json = "{}"
# create an instance of InteropTransactionTypeData from a JSON string
interop_transaction_type_data_instance = InteropTransactionTypeData.from_json(json)
# print the JSON string representation of the object
print InteropTransactionTypeData.to_json()

# convert the object into a dict
interop_transaction_type_data_dict = interop_transaction_type_data_instance.to_dict()
# create an instance of InteropTransactionTypeData from a dict
interop_transaction_type_data_form_dict = interop_transaction_type_data.from_dict(interop_transaction_type_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


