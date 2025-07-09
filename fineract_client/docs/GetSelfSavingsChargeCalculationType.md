# GetSelfSavingsChargeCalculationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_savings_charge_calculation_type import GetSelfSavingsChargeCalculationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsChargeCalculationType from a JSON string
get_self_savings_charge_calculation_type_instance = GetSelfSavingsChargeCalculationType.from_json(json)
# print the JSON string representation of the object
print(GetSelfSavingsChargeCalculationType.to_json())

# convert the object into a dict
get_self_savings_charge_calculation_type_dict = get_self_savings_charge_calculation_type_instance.to_dict()
# create an instance of GetSelfSavingsChargeCalculationType from a dict
get_self_savings_charge_calculation_type_from_dict = GetSelfSavingsChargeCalculationType.from_dict(get_self_savings_charge_calculation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


