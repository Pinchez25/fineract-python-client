# GetIncomeType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_income_type import GetIncomeType

# TODO update the JSON string below
json = "{}"
# create an instance of GetIncomeType from a JSON string
get_income_type_instance = GetIncomeType.from_json(json)
# print the JSON string representation of the object
print(GetIncomeType.to_json())

# convert the object into a dict
get_income_type_dict = get_income_type_instance.to_dict()
# create an instance of GetIncomeType from a dict
get_income_type_from_dict = GetIncomeType.from_dict(get_income_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


