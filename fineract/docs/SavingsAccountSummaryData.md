# SavingsAccountSummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **float** |  | [optional] 
**available_balance** | **float** |  | [optional] 
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**interest_not_posted** | **float** |  | [optional] 
**interest_posted_till_date** | **date** |  | [optional] 
**last_interest_calculation_date** | **date** |  | [optional] 
**prev_interest_posted_till_date** | **date** |  | [optional] 
**running_balance_on_interest_posting_till_date** | **float** |  | [optional] 
**running_balance_on_pivot_date** | **float** |  | [optional] 
**total_annual_fees** | **float** |  | [optional] 
**total_deposits** | **float** |  | [optional] 
**total_fee_charge** | **float** |  | [optional] 
**total_interest_earned** | **float** |  | [optional] 
**total_interest_posted** | **float** |  | [optional] 
**total_overdraft_interest_derived** | **float** |  | [optional] 
**total_penalty_charge** | **float** |  | [optional] 
**total_withdrawal_fees** | **float** |  | [optional] 
**total_withdrawals** | **float** |  | [optional] 
**total_withhold_tax** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_summary_data import SavingsAccountSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountSummaryData from a JSON string
savings_account_summary_data_instance = SavingsAccountSummaryData.from_json(json)
# print the JSON string representation of the object
print(SavingsAccountSummaryData.to_json())

# convert the object into a dict
savings_account_summary_data_dict = savings_account_summary_data_instance.to_dict()
# create an instance of SavingsAccountSummaryData from a dict
savings_account_summary_data_from_dict = SavingsAccountSummaryData.from_dict(savings_account_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


