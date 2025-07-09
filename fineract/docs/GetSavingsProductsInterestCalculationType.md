# GetSavingsProductsInterestCalculationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_interest_calculation_type import GetSavingsProductsInterestCalculationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsInterestCalculationType from a JSON string
get_savings_products_interest_calculation_type_instance = GetSavingsProductsInterestCalculationType.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsInterestCalculationType.to_json())

# convert the object into a dict
get_savings_products_interest_calculation_type_dict = get_savings_products_interest_calculation_type_instance.to_dict()
# create an instance of GetSavingsProductsInterestCalculationType from a dict
get_savings_products_interest_calculation_type_from_dict = GetSavingsProductsInterestCalculationType.from_dict(get_savings_products_interest_calculation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


