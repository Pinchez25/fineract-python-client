# GetClientsSavingProductOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_overdraft** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**withdrawal_fee_for_transfers** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_saving_product_options import GetClientsSavingProductOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsSavingProductOptions from a JSON string
get_clients_saving_product_options_instance = GetClientsSavingProductOptions.from_json(json)
# print the JSON string representation of the object
print GetClientsSavingProductOptions.to_json()

# convert the object into a dict
get_clients_saving_product_options_dict = get_clients_saving_product_options_instance.to_dict()
# create an instance of GetClientsSavingProductOptions from a dict
get_clients_saving_product_options_form_dict = get_clients_saving_product_options.from_dict(get_clients_saving_product_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


