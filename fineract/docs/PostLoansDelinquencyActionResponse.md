# PostLoansDelinquencyActionResponse

PostLoansDelinquencyActionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_delinquency_action_response import PostLoansDelinquencyActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansDelinquencyActionResponse from a JSON string
post_loans_delinquency_action_response_instance = PostLoansDelinquencyActionResponse.from_json(json)
# print the JSON string representation of the object
print(PostLoansDelinquencyActionResponse.to_json())

# convert the object into a dict
post_loans_delinquency_action_response_dict = post_loans_delinquency_action_response_instance.to_dict()
# create an instance of PostLoansDelinquencyActionResponse from a dict
post_loans_delinquency_action_response_from_dict = PostLoansDelinquencyActionResponse.from_dict(post_loans_delinquency_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


