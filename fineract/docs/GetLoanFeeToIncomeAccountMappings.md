# GetLoanFeeToIncomeAccountMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge** | [**GetLoanCharge**](GetLoanCharge.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**income_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_account_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_fee_to_income_account_mappings import GetLoanFeeToIncomeAccountMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanFeeToIncomeAccountMappings from a JSON string
get_loan_fee_to_income_account_mappings_instance = GetLoanFeeToIncomeAccountMappings.from_json(json)
# print the JSON string representation of the object
print(GetLoanFeeToIncomeAccountMappings.to_json())

# convert the object into a dict
get_loan_fee_to_income_account_mappings_dict = get_loan_fee_to_income_account_mappings_instance.to_dict()
# create an instance of GetLoanFeeToIncomeAccountMappings from a dict
get_loan_fee_to_income_account_mappings_from_dict = GetLoanFeeToIncomeAccountMappings.from_dict(get_loan_fee_to_income_account_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


