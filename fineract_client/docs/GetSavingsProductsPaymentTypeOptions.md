# GetSavingsProductsPaymentTypeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_cash_payment** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_payment_type_options import GetSavingsProductsPaymentTypeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsPaymentTypeOptions from a JSON string
get_savings_products_payment_type_options_instance = GetSavingsProductsPaymentTypeOptions.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsPaymentTypeOptions.to_json())

# convert the object into a dict
get_savings_products_payment_type_options_dict = get_savings_products_payment_type_options_instance.to_dict()
# create an instance of GetSavingsProductsPaymentTypeOptions from a dict
get_savings_products_payment_type_options_from_dict = GetSavingsProductsPaymentTypeOptions.from_dict(get_savings_products_payment_type_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


