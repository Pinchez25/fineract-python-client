# GetSavingsProductOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_product_options import GetSavingsProductOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductOptions from a JSON string
get_savings_product_options_instance = GetSavingsProductOptions.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductOptions.to_json())

# convert the object into a dict
get_savings_product_options_dict = get_savings_product_options_instance.to_dict()
# create an instance of GetSavingsProductOptions from a dict
get_savings_product_options_from_dict = GetSavingsProductOptions.from_dict(get_savings_product_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


