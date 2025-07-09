# PostCodeValuesDataRequest

PostCodeValuesDataRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_code_values_data_request import PostCodeValuesDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCodeValuesDataRequest from a JSON string
post_code_values_data_request_instance = PostCodeValuesDataRequest.from_json(json)
# print the JSON string representation of the object
print PostCodeValuesDataRequest.to_json()

# convert the object into a dict
post_code_values_data_request_dict = post_code_values_data_request_instance.to_dict()
# create an instance of PostCodeValuesDataRequest from a dict
post_code_values_data_request_form_dict = post_code_values_data_request.from_dict(post_code_values_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


