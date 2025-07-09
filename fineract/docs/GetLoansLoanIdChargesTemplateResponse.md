# GetLoansLoanIdChargesTemplateResponse

GetLoansLoanIdChargesTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_paid** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**amount_written_off** | **float** |  | [optional] 
**charge_options** | [**List[GetLoanChargeTemplateChargeOptions]**](GetLoanChargeTemplateChargeOptions.md) |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_charges_template_response import GetLoansLoanIdChargesTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdChargesTemplateResponse from a JSON string
get_loans_loan_id_charges_template_response_instance = GetLoansLoanIdChargesTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdChargesTemplateResponse.to_json()

# convert the object into a dict
get_loans_loan_id_charges_template_response_dict = get_loans_loan_id_charges_template_response_instance.to_dict()
# create an instance of GetLoansLoanIdChargesTemplateResponse from a dict
get_loans_loan_id_charges_template_response_form_dict = get_loans_loan_id_charges_template_response.from_dict(get_loans_loan_id_charges_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


