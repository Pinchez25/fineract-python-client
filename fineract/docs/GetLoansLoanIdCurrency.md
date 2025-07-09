# GetLoansLoanIdCurrency


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
from fineract_client.models.get_loans_loan_id_currency import GetLoansLoanIdCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdCurrency from a JSON string
get_loans_loan_id_currency_instance = GetLoansLoanIdCurrency.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdCurrency.to_json()

# convert the object into a dict
get_loans_loan_id_currency_dict = get_loans_loan_id_currency_instance.to_dict()
# create an instance of GetLoansLoanIdCurrency from a dict
get_loans_loan_id_currency_form_dict = get_loans_loan_id_currency.from_dict(get_loans_loan_id_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


