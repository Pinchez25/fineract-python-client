# GetLoanAccountingMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_off_expense_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**charge_off_fraud_expense_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**fund_source_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**goodwill_credit_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_charge_off_fees_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_charge_off_interest_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_charge_off_penalty_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_fee_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_goodwill_credit_fees_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_goodwill_credit_interest_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_goodwill_credit_penalty_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_penalty_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**income_from_recovery_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**interest_on_loan_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**loan_portfolio_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**overpayment_liability_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**receivable_fee_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**receivable_interest_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**receivable_penalty_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**transfers_in_suspense_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 
**write_off_account** | [**GetGlAccountMapping**](GetGlAccountMapping.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_accounting_mappings import GetLoanAccountingMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanAccountingMappings from a JSON string
get_loan_accounting_mappings_instance = GetLoanAccountingMappings.from_json(json)
# print the JSON string representation of the object
print(GetLoanAccountingMappings.to_json())

# convert the object into a dict
get_loan_accounting_mappings_dict = get_loan_accounting_mappings_instance.to_dict()
# create an instance of GetLoanAccountingMappings from a dict
get_loan_accounting_mappings_from_dict = GetLoanAccountingMappings.from_dict(get_loan_accounting_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


