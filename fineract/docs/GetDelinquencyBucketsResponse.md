# GetDelinquencyBucketsResponse

GetDelinquencyBucketsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**ranges** | [**List[GetDelinquencyRangesResponse]**](GetDelinquencyRangesResponse.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_delinquency_buckets_response import GetDelinquencyBucketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDelinquencyBucketsResponse from a JSON string
get_delinquency_buckets_response_instance = GetDelinquencyBucketsResponse.from_json(json)
# print the JSON string representation of the object
print GetDelinquencyBucketsResponse.to_json()

# convert the object into a dict
get_delinquency_buckets_response_dict = get_delinquency_buckets_response_instance.to_dict()
# create an instance of GetDelinquencyBucketsResponse from a dict
get_delinquency_buckets_response_form_dict = get_delinquency_buckets_response.from_dict(get_delinquency_buckets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


