# PostLoansLoanIdChargesChargeIdResponse

PostLoansLoanIdChargesChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PostLoansLoanIdChargesChargeIdChanges**](PostLoansLoanIdChargesChargeIdChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 
**sub_resource_external_id** | **str** |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_charges_charge_id_response import PostLoansLoanIdChargesChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdChargesChargeIdResponse from a JSON string
post_loans_loan_id_charges_charge_id_response_instance = PostLoansLoanIdChargesChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print(PostLoansLoanIdChargesChargeIdResponse.to_json())

# convert the object into a dict
post_loans_loan_id_charges_charge_id_response_dict = post_loans_loan_id_charges_charge_id_response_instance.to_dict()
# create an instance of PostLoansLoanIdChargesChargeIdResponse from a dict
post_loans_loan_id_charges_charge_id_response_from_dict = PostLoansLoanIdChargesChargeIdResponse.from_dict(post_loans_loan_id_charges_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


