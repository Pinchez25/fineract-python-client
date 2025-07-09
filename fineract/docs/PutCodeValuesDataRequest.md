# PutCodeValuesDataRequest

PutCodeValuesDataRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_code_values_data_request import PutCodeValuesDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutCodeValuesDataRequest from a JSON string
put_code_values_data_request_instance = PutCodeValuesDataRequest.from_json(json)
# print the JSON string representation of the object
print(PutCodeValuesDataRequest.to_json())

# convert the object into a dict
put_code_values_data_request_dict = put_code_values_data_request_instance.to_dict()
# create an instance of PutCodeValuesDataRequest from a dict
put_code_values_data_request_from_dict = PutCodeValuesDataRequest.from_dict(put_code_values_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


