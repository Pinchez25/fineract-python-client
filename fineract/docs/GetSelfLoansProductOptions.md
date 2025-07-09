# GetSelfLoansProductOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_loans_product_options import GetSelfLoansProductOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoansProductOptions from a JSON string
get_self_loans_product_options_instance = GetSelfLoansProductOptions.from_json(json)
# print the JSON string representation of the object
print GetSelfLoansProductOptions.to_json()

# convert the object into a dict
get_self_loans_product_options_dict = get_self_loans_product_options_instance.to_dict()
# create an instance of GetSelfLoansProductOptions from a dict
get_self_loans_product_options_form_dict = get_self_loans_product_options.from_dict(get_self_loans_product_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


