# GetEquityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_equity_type import GetEquityType

# TODO update the JSON string below
json = "{}"
# create an instance of GetEquityType from a JSON string
get_equity_type_instance = GetEquityType.from_json(json)
# print the JSON string representation of the object
print(GetEquityType.to_json())

# convert the object into a dict
get_equity_type_dict = get_equity_type_instance.to_dict()
# create an instance of GetEquityType from a dict
get_equity_type_from_dict = GetEquityType.from_dict(get_equity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


