# GetLoansLoanIdCollateralsResponse

GetLoansLoanIdCollateralsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**GetCollateralCurrencyResponse**](GetCollateralCurrencyResponse.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | [**GetCollateralTypeResponse**](GetCollateralTypeResponse.md) |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_collaterals_response import GetLoansLoanIdCollateralsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdCollateralsResponse from a JSON string
get_loans_loan_id_collaterals_response_instance = GetLoansLoanIdCollateralsResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdCollateralsResponse.to_json())

# convert the object into a dict
get_loans_loan_id_collaterals_response_dict = get_loans_loan_id_collaterals_response_instance.to_dict()
# create an instance of GetLoansLoanIdCollateralsResponse from a dict
get_loans_loan_id_collaterals_response_from_dict = GetLoansLoanIdCollateralsResponse.from_dict(get_loans_loan_id_collaterals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


