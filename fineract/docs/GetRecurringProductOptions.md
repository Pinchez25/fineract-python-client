# GetRecurringProductOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_product_options import GetRecurringProductOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringProductOptions from a JSON string
get_recurring_product_options_instance = GetRecurringProductOptions.from_json(json)
# print the JSON string representation of the object
print GetRecurringProductOptions.to_json()

# convert the object into a dict
get_recurring_product_options_dict = get_recurring_product_options_instance.to_dict()
# create an instance of GetRecurringProductOptions from a dict
get_recurring_product_options_form_dict = get_recurring_product_options.from_dict(get_recurring_product_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


