# GetLoansLoanIdChargesChargeIdResponse

GetLoansLoanIdChargesChargeIdResponse

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
**charge_calculation_type** | [**GetLoanChargeCalculationType**](GetLoanChargeCalculationType.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_time_type** | [**GetLoanChargeTimeType**](GetLoanChargeTimeType.md) |  | [optional] 
**currency** | [**GetLoanChargeCurrency**](GetLoanChargeCurrency.md) |  | [optional] 
**due_date** | **date** |  | [optional] 
**external_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_charges_charge_id_response import GetLoansLoanIdChargesChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdChargesChargeIdResponse from a JSON string
get_loans_loan_id_charges_charge_id_response_instance = GetLoansLoanIdChargesChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdChargesChargeIdResponse.to_json()

# convert the object into a dict
get_loans_loan_id_charges_charge_id_response_dict = get_loans_loan_id_charges_charge_id_response_instance.to_dict()
# create an instance of GetLoansLoanIdChargesChargeIdResponse from a dict
get_loans_loan_id_charges_charge_id_response_form_dict = get_loans_loan_id_charges_charge_id_response.from_dict(get_loans_loan_id_charges_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


