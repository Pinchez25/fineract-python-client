# GetLoansLoanIdPaymentType

List of GetLoansLoanIdPaymentType

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
from fineract_client.models.get_loans_loan_id_payment_type import GetLoansLoanIdPaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdPaymentType from a JSON string
get_loans_loan_id_payment_type_instance = GetLoansLoanIdPaymentType.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdPaymentType.to_json())

# convert the object into a dict
get_loans_loan_id_payment_type_dict = get_loans_loan_id_payment_type_instance.to_dict()
# create an instance of GetLoansLoanIdPaymentType from a dict
get_loans_loan_id_payment_type_from_dict = GetLoansLoanIdPaymentType.from_dict(get_loans_loan_id_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


