# DelinquencyRangeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**maximum_age_days** | **int** |  | [optional] 
**minimum_age_days** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delinquency_range_data import DelinquencyRangeData

# TODO update the JSON string below
json = "{}"
# create an instance of DelinquencyRangeData from a JSON string
delinquency_range_data_instance = DelinquencyRangeData.from_json(json)
# print the JSON string representation of the object
print(DelinquencyRangeData.to_json())

# convert the object into a dict
delinquency_range_data_dict = delinquency_range_data_instance.to_dict()
# create an instance of DelinquencyRangeData from a dict
delinquency_range_data_from_dict = DelinquencyRangeData.from_dict(delinquency_range_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


