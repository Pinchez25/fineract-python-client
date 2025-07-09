# GetLoanProductsPaymentTypeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_payment_type_options import GetLoanProductsPaymentTypeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsPaymentTypeOptions from a JSON string
get_loan_products_payment_type_options_instance = GetLoanProductsPaymentTypeOptions.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsPaymentTypeOptions.to_json())

# convert the object into a dict
get_loan_products_payment_type_options_dict = get_loan_products_payment_type_options_instance.to_dict()
# create an instance of GetLoanProductsPaymentTypeOptions from a dict
get_loan_products_payment_type_options_from_dict = GetLoanProductsPaymentTypeOptions.from_dict(get_loan_products_payment_type_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


