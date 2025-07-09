# TransactionTypeEnumData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.transaction_type_enum_data import TransactionTypeEnumData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionTypeEnumData from a JSON string
transaction_type_enum_data_instance = TransactionTypeEnumData.from_json(json)
# print the JSON string representation of the object
print(TransactionTypeEnumData.to_json())

# convert the object into a dict
transaction_type_enum_data_dict = transaction_type_enum_data_instance.to_dict()
# create an instance of TransactionTypeEnumData from a dict
transaction_type_enum_data_from_dict = TransactionTypeEnumData.from_dict(transaction_type_enum_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


