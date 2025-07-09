# PutDelinquencyBucketResponse

PutDelinquencyBucketResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_delinquency_bucket_response import PutDelinquencyBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutDelinquencyBucketResponse from a JSON string
put_delinquency_bucket_response_instance = PutDelinquencyBucketResponse.from_json(json)
# print the JSON string representation of the object
print(PutDelinquencyBucketResponse.to_json())

# convert the object into a dict
put_delinquency_bucket_response_dict = put_delinquency_bucket_response_instance.to_dict()
# create an instance of PutDelinquencyBucketResponse from a dict
put_delinquency_bucket_response_from_dict = PutDelinquencyBucketResponse.from_dict(put_delinquency_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


