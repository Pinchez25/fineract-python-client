# LoanProductFloatingRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_differential_lending_rate** | **float** |  | [optional] 
**floating_interest_rate_calculation_allowed** | **bool** |  | [optional] 
**floating_rate** | [**FloatingRate**](FloatingRate.md) |  | [optional] 
**id** | **int** |  | [optional] 
**interest_rate_differential** | **float** |  | [optional] 
**loan_product** | [**LoanProduct**](LoanProduct.md) |  | [optional] 
**max_differential_lending_rate** | **float** |  | [optional] 
**min_differential_lending_rate** | **float** |  | [optional] 
**new** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_floating_rates import LoanProductFloatingRates

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductFloatingRates from a JSON string
loan_product_floating_rates_instance = LoanProductFloatingRates.from_json(json)
# print the JSON string representation of the object
print(LoanProductFloatingRates.to_json())

# convert the object into a dict
loan_product_floating_rates_dict = loan_product_floating_rates_instance.to_dict()
# create an instance of LoanProductFloatingRates from a dict
loan_product_floating_rates_from_dict = LoanProductFloatingRates.from_dict(loan_product_floating_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


