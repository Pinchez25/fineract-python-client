# PutCodeValueDataResponse

PutCodeValueDataResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutCodeValuechangesSwagger**](PutCodeValuechangesSwagger.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_code_value_data_response import PutCodeValueDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutCodeValueDataResponse from a JSON string
put_code_value_data_response_instance = PutCodeValueDataResponse.from_json(json)
# print the JSON string representation of the object
print(PutCodeValueDataResponse.to_json())

# convert the object into a dict
put_code_value_data_response_dict = put_code_value_data_response_instance.to_dict()
# create an instance of PutCodeValueDataResponse from a dict
put_code_value_data_response_from_dict = PutCodeValueDataResponse.from_dict(put_code_value_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


