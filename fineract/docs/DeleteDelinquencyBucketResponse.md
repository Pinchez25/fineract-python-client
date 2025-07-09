# DeleteDelinquencyBucketResponse

DeleteDelinquencyBucketResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_delinquency_bucket_response import DeleteDelinquencyBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDelinquencyBucketResponse from a JSON string
delete_delinquency_bucket_response_instance = DeleteDelinquencyBucketResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteDelinquencyBucketResponse.to_json())

# convert the object into a dict
delete_delinquency_bucket_response_dict = delete_delinquency_bucket_response_instance.to_dict()
# create an instance of DeleteDelinquencyBucketResponse from a dict
delete_delinquency_bucket_response_from_dict = DeleteDelinquencyBucketResponse.from_dict(delete_delinquency_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


