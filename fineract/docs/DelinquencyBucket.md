# DelinquencyBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** |  | 
**created_date** | **datetime** |  | 
**created_date_time** | **datetime** |  | 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | 
**last_modified_date** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**ranges** | [**List[DelinquencyRange]**](DelinquencyRange.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delinquency_bucket import DelinquencyBucket

# TODO update the JSON string below
json = "{}"
# create an instance of DelinquencyBucket from a JSON string
delinquency_bucket_instance = DelinquencyBucket.from_json(json)
# print the JSON string representation of the object
print DelinquencyBucket.to_json()

# convert the object into a dict
delinquency_bucket_dict = delinquency_bucket_instance.to_dict()
# create an instance of DelinquencyBucket from a dict
delinquency_bucket_form_dict = delinquency_bucket.from_dict(delinquency_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


