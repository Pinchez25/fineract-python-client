# GetFixedDepositProductsGlAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_products_gl_account import GetFixedDepositProductsGlAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositProductsGlAccount from a JSON string
get_fixed_deposit_products_gl_account_instance = GetFixedDepositProductsGlAccount.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositProductsGlAccount.to_json())

# convert the object into a dict
get_fixed_deposit_products_gl_account_dict = get_fixed_deposit_products_gl_account_instance.to_dict()
# create an instance of GetFixedDepositProductsGlAccount from a dict
get_fixed_deposit_products_gl_account_from_dict = GetFixedDepositProductsGlAccount.from_dict(get_fixed_deposit_products_gl_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


