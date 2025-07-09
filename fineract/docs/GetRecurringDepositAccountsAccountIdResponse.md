# GetRecurringDepositAccountsAccountIdResponse

GetRecurringDepositAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_chart** | [**GetRecurringDepositAccountsAccountChart**](GetRecurringDepositAccountsAccountChart.md) |  | [optional] 
**account_no** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**GetRecurringDepositAccountsCurrency**](GetRecurringDepositAccountsCurrency.md) |  | [optional] 
**deposit_period** | **int** |  | [optional] 
**deposit_period_frequency** | [**GetRecurringDepositAccountsDepositPeriodFrequency**](GetRecurringDepositAccountsDepositPeriodFrequency.md) |  | [optional] 
**expected_first_deposit_on_date** | **date** |  | [optional] 
**external_id** | **str** |  | [optional] 
**field_officer_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetRecurringDepositAccountsInterestCalculationDaysInYearType**](GetRecurringDepositAccountsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetRecurringDepositAccountsInterestCalculationType**](GetRecurringDepositAccountsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetRecurringDepositAccountsInterestCompoundingPeriodType**](GetRecurringDepositAccountsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetRecurringDepositAccountsInterestPostingPeriodType**](GetRecurringDepositAccountsInterestPostingPeriodType.md) |  | [optional] 
**max_deposit_term** | **int** |  | [optional] 
**max_deposit_term_type** | [**GetRecurringDepositAccountsMaxDepositTermType**](GetRecurringDepositAccountsMaxDepositTermType.md) |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type** | [**GetRecurringDepositAccountsMinDepositTermType**](GetRecurringDepositAccountsMinDepositTermType.md) |  | [optional] 
**pre_closure_penal_applicable** | **bool** |  | [optional] 
**recurring_deposit_amount** | **int** |  | [optional] 
**recurring_deposit_frequency** | **int** |  | [optional] 
**recurring_deposit_frequency_type** | [**GetRecurringDepositAccountsRecurringDepositFrequencyType**](GetRecurringDepositAccountsRecurringDepositFrequencyType.md) |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 
**status** | [**GetRecurringDepositAccountsStatus**](GetRecurringDepositAccountsStatus.md) |  | [optional] 
**summary** | [**GetRecurringDepositAccountsSummary**](GetRecurringDepositAccountsSummary.md) |  | [optional] 
**timeline** | [**GetRecurringDepositAccountsTimeline**](GetRecurringDepositAccountsTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_account_id_response import GetRecurringDepositAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsAccountIdResponse from a JSON string
get_recurring_deposit_accounts_account_id_response_instance = GetRecurringDepositAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecurringDepositAccountsAccountIdResponse.to_json())

# convert the object into a dict
get_recurring_deposit_accounts_account_id_response_dict = get_recurring_deposit_accounts_account_id_response_instance.to_dict()
# create an instance of GetRecurringDepositAccountsAccountIdResponse from a dict
get_recurring_deposit_accounts_account_id_response_from_dict = GetRecurringDepositAccountsAccountIdResponse.from_dict(get_recurring_deposit_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


