# GetSelfClientsChargeCalculationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_charge_calculation_type import GetSelfClientsChargeCalculationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsChargeCalculationType from a JSON string
get_self_clients_charge_calculation_type_instance = GetSelfClientsChargeCalculationType.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsChargeCalculationType.to_json())

# convert the object into a dict
get_self_clients_charge_calculation_type_dict = get_self_clients_charge_calculation_type_instance.to_dict()
# create an instance of GetSelfClientsChargeCalculationType from a dict
get_self_clients_charge_calculation_type_from_dict = GetSelfClientsChargeCalculationType.from_dict(get_self_clients_charge_calculation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


