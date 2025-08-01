# PostStandingInstructionsRequest

PostStandingInstructionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**from_account_id** | **int** |  | [optional] 
**from_account_type** | **int** |  | [optional] 
**from_client_id** | **int** |  | [optional] 
**from_office_id** | **int** |  | [optional] 
**instruction_type** | **int** |  | [optional] 
**locale** | **str** | en | [optional] 
**month_day_format** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**recurrence_frequency** | **int** |  | [optional] 
**recurrence_interval** | **int** |  | [optional] 
**recurrence_on_month_day** | **str** |  | [optional] 
**recurrence_type** | **int** |  | [optional] 
**status** | **int** |  | [optional] 
**to_account_id** | **int** |  | [optional] 
**to_account_type** | **int** |  | [optional] 
**to_client_id** | **int** |  | [optional] 
**to_office_id** | **int** |  | [optional] 
**transfer_type** | **int** |  | [optional] 
**valid_from** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_standing_instructions_request import PostStandingInstructionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostStandingInstructionsRequest from a JSON string
post_standing_instructions_request_instance = PostStandingInstructionsRequest.from_json(json)
# print the JSON string representation of the object
print(PostStandingInstructionsRequest.to_json())

# convert the object into a dict
post_standing_instructions_request_dict = post_standing_instructions_request_instance.to_dict()
# create an instance of PostStandingInstructionsRequest from a dict
post_standing_instructions_request_from_dict = PostStandingInstructionsRequest.from_dict(post_standing_instructions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


