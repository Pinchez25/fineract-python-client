# GetLoansTemplateProductOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_template_product_options import GetLoansTemplateProductOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansTemplateProductOptions from a JSON string
get_loans_template_product_options_instance = GetLoansTemplateProductOptions.from_json(json)
# print the JSON string representation of the object
print(GetLoansTemplateProductOptions.to_json())

# convert the object into a dict
get_loans_template_product_options_dict = get_loans_template_product_options_instance.to_dict()
# create an instance of GetLoansTemplateProductOptions from a dict
get_loans_template_product_options_from_dict = GetLoansTemplateProductOptions.from_dict(get_loans_template_product_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


