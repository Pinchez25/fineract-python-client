# GetSavingsProductsChargeAppliesTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_charge_applies_to import GetSavingsProductsChargeAppliesTo

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsChargeAppliesTo from a JSON string
get_savings_products_charge_applies_to_instance = GetSavingsProductsChargeAppliesTo.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsChargeAppliesTo.to_json())

# convert the object into a dict
get_savings_products_charge_applies_to_dict = get_savings_products_charge_applies_to_instance.to_dict()
# create an instance of GetSavingsProductsChargeAppliesTo from a dict
get_savings_products_charge_applies_to_from_dict = GetSavingsProductsChargeAppliesTo.from_dict(get_savings_products_charge_applies_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


