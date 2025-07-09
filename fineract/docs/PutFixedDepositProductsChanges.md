# PutFixedDepositProductsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_fixed_deposit_products_changes import PutFixedDepositProductsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutFixedDepositProductsChanges from a JSON string
put_fixed_deposit_products_changes_instance = PutFixedDepositProductsChanges.from_json(json)
# print the JSON string representation of the object
print(PutFixedDepositProductsChanges.to_json())

# convert the object into a dict
put_fixed_deposit_products_changes_dict = put_fixed_deposit_products_changes_instance.to_dict()
# create an instance of PutFixedDepositProductsChanges from a dict
put_fixed_deposit_products_changes_from_dict = PutFixedDepositProductsChanges.from_dict(put_fixed_deposit_products_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


