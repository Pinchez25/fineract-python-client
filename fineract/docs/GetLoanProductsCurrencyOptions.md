# GetLoanProductsCurrencyOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**decimal_places** | **int** |  | [optional] 
**display_label** | **str** |  | [optional] 
**display_symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_currency_options import GetLoanProductsCurrencyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsCurrencyOptions from a JSON string
get_loan_products_currency_options_instance = GetLoanProductsCurrencyOptions.from_json(json)
# print the JSON string representation of the object
print GetLoanProductsCurrencyOptions.to_json()

# convert the object into a dict
get_loan_products_currency_options_dict = get_loan_products_currency_options_instance.to_dict()
# create an instance of GetLoanProductsCurrencyOptions from a dict
get_loan_products_currency_options_form_dict = get_loan_products_currency_options.from_dict(get_loan_products_currency_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


