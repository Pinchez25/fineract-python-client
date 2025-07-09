# GetSelfClientsChargeTimeType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_charge_time_type import GetSelfClientsChargeTimeType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsChargeTimeType from a JSON string
get_self_clients_charge_time_type_instance = GetSelfClientsChargeTimeType.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsChargeTimeType.to_json())

# convert the object into a dict
get_self_clients_charge_time_type_dict = get_self_clients_charge_time_type_instance.to_dict()
# create an instance of GetSelfClientsChargeTimeType from a dict
get_self_clients_charge_time_type_from_dict = GetSelfClientsChargeTimeType.from_dict(get_self_clients_charge_time_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


