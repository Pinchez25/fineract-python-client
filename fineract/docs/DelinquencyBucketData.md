# DelinquencyBucketData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**ranges** | [**List[DelinquencyRangeData]**](DelinquencyRangeData.md) |  | [optional] 

## Example

```python
from fineract_client.models.delinquency_bucket_data import DelinquencyBucketData

# TODO update the JSON string below
json = "{}"
# create an instance of DelinquencyBucketData from a JSON string
delinquency_bucket_data_instance = DelinquencyBucketData.from_json(json)
# print the JSON string representation of the object
print DelinquencyBucketData.to_json()

# convert the object into a dict
delinquency_bucket_data_dict = delinquency_bucket_data_instance.to_dict()
# create an instance of DelinquencyBucketData from a dict
delinquency_bucket_data_form_dict = delinquency_bucket_data.from_dict(delinquency_bucket_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


