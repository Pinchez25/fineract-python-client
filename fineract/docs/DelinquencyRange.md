# DelinquencyRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** |  | [optional] 
**created_by** | **int** |  | 
**created_date** | **datetime** |  | 
**created_date_time** | **datetime** |  | 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | 
**last_modified_date** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**maximum_age_days** | **int** |  | [optional] 
**minimum_age_days** | **int** |  | [optional] 
**new** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delinquency_range import DelinquencyRange

# TODO update the JSON string below
json = "{}"
# create an instance of DelinquencyRange from a JSON string
delinquency_range_instance = DelinquencyRange.from_json(json)
# print the JSON string representation of the object
print DelinquencyRange.to_json()

# convert the object into a dict
delinquency_range_dict = delinquency_range_instance.to_dict()
# create an instance of DelinquencyRange from a dict
delinquency_range_form_dict = delinquency_range.from_dict(delinquency_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


