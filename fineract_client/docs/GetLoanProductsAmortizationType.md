# GetLoanProductsAmortizationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_amortization_type import GetLoanProductsAmortizationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsAmortizationType from a JSON string
get_loan_products_amortization_type_instance = GetLoanProductsAmortizationType.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsAmortizationType.to_json())

# convert the object into a dict
get_loan_products_amortization_type_dict = get_loan_products_amortization_type_instance.to_dict()
# create an instance of GetLoanProductsAmortizationType from a dict
get_loan_products_amortization_type_from_dict = GetLoanProductsAmortizationType.from_dict(get_loan_products_amortization_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


