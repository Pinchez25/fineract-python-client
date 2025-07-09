# GetClientChargeTimeType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_client_charge_time_type import GetClientChargeTimeType

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientChargeTimeType from a JSON string
get_client_charge_time_type_instance = GetClientChargeTimeType.from_json(json)
# print the JSON string representation of the object
print(GetClientChargeTimeType.to_json())

# convert the object into a dict
get_client_charge_time_type_dict = get_client_charge_time_type_instance.to_dict()
# create an instance of GetClientChargeTimeType from a dict
get_client_charge_time_type_from_dict = GetClientChargeTimeType.from_dict(get_client_charge_time_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


