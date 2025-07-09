# GetFundsResponse

GetFundsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_funds_response import GetFundsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFundsResponse from a JSON string
get_funds_response_instance = GetFundsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFundsResponse.to_json())

# convert the object into a dict
get_funds_response_dict = get_funds_response_instance.to_dict()
# create an instance of GetFundsResponse from a dict
get_funds_response_from_dict = GetFundsResponse.from_dict(get_funds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


