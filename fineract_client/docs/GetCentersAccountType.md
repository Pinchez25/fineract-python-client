# GetCentersAccountType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_account_type import GetCentersAccountType

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersAccountType from a JSON string
get_centers_account_type_instance = GetCentersAccountType.from_json(json)
# print the JSON string representation of the object
print(GetCentersAccountType.to_json())

# convert the object into a dict
get_centers_account_type_dict = get_centers_account_type_instance.to_dict()
# create an instance of GetCentersAccountType from a dict
get_centers_account_type_from_dict = GetCentersAccountType.from_dict(get_centers_account_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


