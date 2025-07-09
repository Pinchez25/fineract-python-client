# GetLoansApprovalTemplateResponse

GetLoansApprovalTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_amount** | **float** |  | [optional] 
**approval_date** | **date** |  | [optional] 
**currency** | [**GetLoanCurrency**](GetLoanCurrency.md) |  | [optional] 
**net_disbursal_amount** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_approval_template_response import GetLoansApprovalTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansApprovalTemplateResponse from a JSON string
get_loans_approval_template_response_instance = GetLoansApprovalTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoansApprovalTemplateResponse.to_json())

# convert the object into a dict
get_loans_approval_template_response_dict = get_loans_approval_template_response_instance.to_dict()
# create an instance of GetLoansApprovalTemplateResponse from a dict
get_loans_approval_template_response_from_dict = GetLoansApprovalTemplateResponse.from_dict(get_loans_approval_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


