# PostSelfLoansDisbursementData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_principal** | **int** |  | [optional] 
**expected_disbursement_date** | **str** |  | [optional] 
**principal** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_loans_disbursement_data import PostSelfLoansDisbursementData

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfLoansDisbursementData from a JSON string
post_self_loans_disbursement_data_instance = PostSelfLoansDisbursementData.from_json(json)
# print the JSON string representation of the object
print PostSelfLoansDisbursementData.to_json()

# convert the object into a dict
post_self_loans_disbursement_data_dict = post_self_loans_disbursement_data_instance.to_dict()
# create an instance of PostSelfLoansDisbursementData from a dict
post_self_loans_disbursement_data_form_dict = post_self_loans_disbursement_data.from_dict(post_self_loans_disbursement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


