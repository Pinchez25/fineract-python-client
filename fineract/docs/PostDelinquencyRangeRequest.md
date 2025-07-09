# PostDelinquencyRangeRequest

PostDelinquencyRangeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**maximum_age_days** | **int** |  | [optional] 
**minimum_age_days** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_delinquency_range_request import PostDelinquencyRangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDelinquencyRangeRequest from a JSON string
post_delinquency_range_request_instance = PostDelinquencyRangeRequest.from_json(json)
# print the JSON string representation of the object
print PostDelinquencyRangeRequest.to_json()

# convert the object into a dict
post_delinquency_range_request_dict = post_delinquency_range_request_instance.to_dict()
# create an instance of PostDelinquencyRangeRequest from a dict
post_delinquency_range_request_form_dict = post_delinquency_range_request.from_dict(post_delinquency_range_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


