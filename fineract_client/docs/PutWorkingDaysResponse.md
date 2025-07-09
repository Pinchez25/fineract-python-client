# PutWorkingDaysResponse

PutWorkingDaysResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_working_days_response import PutWorkingDaysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutWorkingDaysResponse from a JSON string
put_working_days_response_instance = PutWorkingDaysResponse.from_json(json)
# print the JSON string representation of the object
print(PutWorkingDaysResponse.to_json())

# convert the object into a dict
put_working_days_response_dict = put_working_days_response_instance.to_dict()
# create an instance of PutWorkingDaysResponse from a dict
put_working_days_response_from_dict = PutWorkingDaysResponse.from_dict(put_working_days_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


