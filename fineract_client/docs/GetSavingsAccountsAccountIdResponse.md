# GetSavingsAccountsAccountIdResponse

GetSavingsAccountsAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**GetSavingsCurrency**](GetSavingsCurrency.md) |  | [optional] 
**field_officer_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetSavingsInterestCalculationDaysInYearType**](GetSavingsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetSavingsInterestCalculationType**](GetSavingsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetSavingsInterestCompoundingPeriodType**](GetSavingsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetSavingsInterestPostingPeriodType**](GetSavingsInterestPostingPeriodType.md) |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 
**status** | [**GetSavingsStatus**](GetSavingsStatus.md) |  | [optional] 
**summary** | [**GetSavingsAccountsSummary**](GetSavingsAccountsSummary.md) |  | [optional] 
**timeline** | [**GetSavingsTimeline**](GetSavingsTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_accounts_account_id_response import GetSavingsAccountsAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAccountsAccountIdResponse from a JSON string
get_savings_accounts_account_id_response_instance = GetSavingsAccountsAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetSavingsAccountsAccountIdResponse.to_json())

# convert the object into a dict
get_savings_accounts_account_id_response_dict = get_savings_accounts_account_id_response_instance.to_dict()
# create an instance of GetSavingsAccountsAccountIdResponse from a dict
get_savings_accounts_account_id_response_from_dict = GetSavingsAccountsAccountIdResponse.from_dict(get_savings_accounts_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


