# GetLoansLoanIdCollateralsTemplateResponse

GetLoansLoanIdCollateralsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_collateral_types** | [**List[GetCollateralsTemplateAllowedTypes]**](GetCollateralsTemplateAllowedTypes.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_collaterals_template_response import GetLoansLoanIdCollateralsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdCollateralsTemplateResponse from a JSON string
get_loans_loan_id_collaterals_template_response_instance = GetLoansLoanIdCollateralsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdCollateralsTemplateResponse.to_json())

# convert the object into a dict
get_loans_loan_id_collaterals_template_response_dict = get_loans_loan_id_collaterals_template_response_instance.to_dict()
# create an instance of GetLoansLoanIdCollateralsTemplateResponse from a dict
get_loans_loan_id_collaterals_template_response_from_dict = GetLoansLoanIdCollateralsTemplateResponse.from_dict(get_loans_loan_id_collaterals_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


