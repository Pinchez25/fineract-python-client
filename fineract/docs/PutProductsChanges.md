# PutProductsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_products_changes import PutProductsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutProductsChanges from a JSON string
put_products_changes_instance = PutProductsChanges.from_json(json)
# print the JSON string representation of the object
print PutProductsChanges.to_json()

# convert the object into a dict
put_products_changes_dict = put_products_changes_instance.to_dict()
# create an instance of PutProductsChanges from a dict
put_products_changes_form_dict = put_products_changes.from_dict(put_products_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


