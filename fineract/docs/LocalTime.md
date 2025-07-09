# LocalTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** |  | [optional] 
**minute** | **int** |  | [optional] 
**nano** | **int** |  | [optional] 
**second** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.local_time import LocalTime

# TODO update the JSON string below
json = "{}"
# create an instance of LocalTime from a JSON string
local_time_instance = LocalTime.from_json(json)
# print the JSON string representation of the object
print LocalTime.to_json()

# convert the object into a dict
local_time_dict = local_time_instance.to_dict()
# create an instance of LocalTime from a dict
local_time_form_dict = local_time.from_dict(local_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


