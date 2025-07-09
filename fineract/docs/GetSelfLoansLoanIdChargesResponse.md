# GetSelfLoansLoanIdChargesResponse

GetSelfLoansLoanIdChargesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**amount_or_percentage** | **float** |  | [optional] 
**amount_outstanding** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**amount_percentage_applied_to** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**amount_written_off** | **float** |  | [optional] 
**charge_calculation_type** | [**GetSelfLoansChargeCalculationType**](GetSelfLoansChargeCalculationType.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_time_type** | [**GetSelfLoansChargeTimeType**](GetSelfLoansChargeTimeType.md) |  | [optional] 
**currency** | [**GetLoanCurrency**](GetLoanCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_loans_loan_id_charges_response import GetSelfLoansLoanIdChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoansLoanIdChargesResponse from a JSON string
get_self_loans_loan_id_charges_response_instance = GetSelfLoansLoanIdChargesResponse.from_json(json)
# print the JSON string representation of the object
print(GetSelfLoansLoanIdChargesResponse.to_json())

# convert the object into a dict
get_self_loans_loan_id_charges_response_dict = get_self_loans_loan_id_charges_response_instance.to_dict()
# create an instance of GetSelfLoansLoanIdChargesResponse from a dict
get_self_loans_loan_id_charges_response_from_dict = GetSelfLoansLoanIdChargesResponse.from_dict(get_self_loans_loan_id_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


