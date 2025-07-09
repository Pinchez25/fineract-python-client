# PostSelfLoansResponse

PostSelfLoansResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_loans_response import PostSelfLoansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfLoansResponse from a JSON string
post_self_loans_response_instance = PostSelfLoansResponse.from_json(json)
# print the JSON string representation of the object
print(PostSelfLoansResponse.to_json())

# convert the object into a dict
post_self_loans_response_dict = post_self_loans_response_instance.to_dict()
# create an instance of PostSelfLoansResponse from a dict
post_self_loans_response_from_dict = PostSelfLoansResponse.from_dict(post_self_loans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


