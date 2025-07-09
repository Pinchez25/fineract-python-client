# GetSelfSavingsAccountsResponse

GetSelfSavingsAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**GetSelfSavingsCurrency**](GetSelfSavingsCurrency.md) |  | [optional] 
**field_officer_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetSelfSavingsInterestCalculationDaysInYearType**](GetSelfSavingsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetSelfSavingsInterestCalculationType**](GetSelfSavingsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetSelfSavingsInterestCompoundingPeriodType**](GetSelfSavingsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_posting_period_type** | [**GetSelfSavingsInterestPostingPeriodType**](GetSelfSavingsInterestPostingPeriodType.md) |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 
**status** | [**GetSelfSavingsStatus**](GetSelfSavingsStatus.md) |  | [optional] 
**summary** | [**GetSelfSavingsSummary**](GetSelfSavingsSummary.md) |  | [optional] 
**timeline** | [**GetSelfSavingsTimeline**](GetSelfSavingsTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_savings_accounts_response import GetSelfSavingsAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsAccountsResponse from a JSON string
get_self_savings_accounts_response_instance = GetSelfSavingsAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSelfSavingsAccountsResponse.to_json())

# convert the object into a dict
get_self_savings_accounts_response_dict = get_self_savings_accounts_response_instance.to_dict()
# create an instance of GetSelfSavingsAccountsResponse from a dict
get_self_savings_accounts_response_from_dict = GetSelfSavingsAccountsResponse.from_dict(get_self_savings_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


