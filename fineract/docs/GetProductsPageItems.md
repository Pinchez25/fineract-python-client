# GetProductsPageItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**total_shares** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_products_page_items import GetProductsPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsPageItems from a JSON string
get_products_page_items_instance = GetProductsPageItems.from_json(json)
# print the JSON string representation of the object
print GetProductsPageItems.to_json()

# convert the object into a dict
get_products_page_items_dict = get_products_page_items_instance.to_dict()
# create an instance of GetProductsPageItems from a dict
get_products_page_items_form_dict = get_products_page_items.from_dict(get_products_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


