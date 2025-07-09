# GetCodeValuesDataResponse

GetCodeValuesDataResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_code_values_data_response import GetCodeValuesDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCodeValuesDataResponse from a JSON string
get_code_values_data_response_instance = GetCodeValuesDataResponse.from_json(json)
# print the JSON string representation of the object
print GetCodeValuesDataResponse.to_json()

# convert the object into a dict
get_code_values_data_response_dict = get_code_values_data_response_instance.to_dict()
# create an instance of GetCodeValuesDataResponse from a dict
get_code_values_data_response_form_dict = get_code_values_data_response.from_dict(get_code_values_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


