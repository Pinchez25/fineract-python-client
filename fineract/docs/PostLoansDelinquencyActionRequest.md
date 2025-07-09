# PostLoansDelinquencyActionRequest

PostLoansDelinquencyActionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_delinquency_action_request import PostLoansDelinquencyActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansDelinquencyActionRequest from a JSON string
post_loans_delinquency_action_request_instance = PostLoansDelinquencyActionRequest.from_json(json)
# print the JSON string representation of the object
print PostLoansDelinquencyActionRequest.to_json()

# convert the object into a dict
post_loans_delinquency_action_request_dict = post_loans_delinquency_action_request_instance.to_dict()
# create an instance of PostLoansDelinquencyActionRequest from a dict
post_loans_delinquency_action_request_form_dict = post_loans_delinquency_action_request.from_dict(post_loans_delinquency_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


