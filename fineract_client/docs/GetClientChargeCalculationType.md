# GetClientChargeCalculationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_client_charge_calculation_type import GetClientChargeCalculationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientChargeCalculationType from a JSON string
get_client_charge_calculation_type_instance = GetClientChargeCalculationType.from_json(json)
# print the JSON string representation of the object
print(GetClientChargeCalculationType.to_json())

# convert the object into a dict
get_client_charge_calculation_type_dict = get_client_charge_calculation_type_instance.to_dict()
# create an instance of GetClientChargeCalculationType from a dict
get_client_charge_calculation_type_from_dict = GetClientChargeCalculationType.from_dict(get_client_charge_calculation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


