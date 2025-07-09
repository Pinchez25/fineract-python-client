# IsCatchUpRunningResponse

IsCatchUpRunningResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_catch_up_running** | **bool** |  | [optional] 
**processing_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.is_catch_up_running_response import IsCatchUpRunningResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IsCatchUpRunningResponse from a JSON string
is_catch_up_running_response_instance = IsCatchUpRunningResponse.from_json(json)
# print the JSON string representation of the object
print(IsCatchUpRunningResponse.to_json())

# convert the object into a dict
is_catch_up_running_response_dict = is_catch_up_running_response_instance.to_dict()
# create an instance of IsCatchUpRunningResponse from a dict
is_catch_up_running_response_from_dict = IsCatchUpRunningResponse.from_dict(is_catch_up_running_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


