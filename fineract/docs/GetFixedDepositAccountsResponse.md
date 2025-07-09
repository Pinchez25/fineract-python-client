# GetFixedDepositAccountsResponse

GetFixedDepositAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**GetFixedDepositAccountsCurrency**](GetFixedDepositAccountsCurrency.md) |  | [optional] 
**deposit_amount** | **float** |  | [optional] 
**deposit_period** | **int** |  | [optional] 
**deposit_period_frequency** | [**GetFixedDepositAccountsDepositPeriodFrequency**](GetFixedDepositAccountsDepositPeriodFrequency.md) |  | [optional] 
**field_officer_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**GetFixedDepositAccountsInterestCalculationDaysInYearType**](GetFixedDepositAccountsInterestCalculationDaysInYearType.md) |  | [optional] 
**interest_calculation_type** | [**GetFixedDepositAccountsInterestCalculationType**](GetFixedDepositAccountsInterestCalculationType.md) |  | [optional] 
**interest_compounding_period_type** | [**GetFixedDepositAccountsInterestCompoundingPeriodType**](GetFixedDepositAccountsInterestCompoundingPeriodType.md) |  | [optional] 
**interest_free_period_applicable** | **bool** |  | [optional] 
**interest_posting_period_type** | [**GetFixedDepositAccountsInterestPostingPeriodType**](GetFixedDepositAccountsInterestPostingPeriodType.md) |  | [optional] 
**maturity_amount** | **float** |  | [optional] 
**maturity_date** | **date** |  | [optional] 
**max_deposit_term** | **int** |  | [optional] 
**max_deposit_term_type** | [**GetFixedDepositAccountsMaxDepositTermType**](GetFixedDepositAccountsMaxDepositTermType.md) |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type** | [**GetFixedDepositAccountsMinDepositTermType**](GetFixedDepositAccountsMinDepositTermType.md) |  | [optional] 
**pre_closure_penal_applicable** | **bool** |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 
**status** | [**GetFixedDepositAccountsStatus**](GetFixedDepositAccountsStatus.md) |  | [optional] 
**summary** | [**GetFixedDepositAccountsSummary**](GetFixedDepositAccountsSummary.md) |  | [optional] 
**timeline** | [**GetFixedDepositAccountsTimeline**](GetFixedDepositAccountsTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_response import GetFixedDepositAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsResponse from a JSON string
get_fixed_deposit_accounts_response_instance = GetFixedDepositAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositAccountsResponse.to_json())

# convert the object into a dict
get_fixed_deposit_accounts_response_dict = get_fixed_deposit_accounts_response_instance.to_dict()
# create an instance of GetFixedDepositAccountsResponse from a dict
get_fixed_deposit_accounts_response_from_dict = GetFixedDepositAccountsResponse.from_dict(get_fixed_deposit_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


