# GetCentersDepositType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_deposit_type import GetCentersDepositType

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersDepositType from a JSON string
get_centers_deposit_type_instance = GetCentersDepositType.from_json(json)
# print the JSON string representation of the object
print GetCentersDepositType.to_json()

# convert the object into a dict
get_centers_deposit_type_dict = get_centers_deposit_type_instance.to_dict()
# create an instance of GetCentersDepositType from a dict
get_centers_deposit_type_form_dict = get_centers_deposit_type.from_dict(get_centers_deposit_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


