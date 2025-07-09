# GetClientIdProductIdChargeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_options** | [**GetShareAccountsChargeOptions**](GetShareAccountsChargeOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_client_id_product_id_charge_options import GetClientIdProductIdChargeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientIdProductIdChargeOptions from a JSON string
get_client_id_product_id_charge_options_instance = GetClientIdProductIdChargeOptions.from_json(json)
# print the JSON string representation of the object
print GetClientIdProductIdChargeOptions.to_json()

# convert the object into a dict
get_client_id_product_id_charge_options_dict = get_client_id_product_id_charge_options_instance.to_dict()
# create an instance of GetClientIdProductIdChargeOptions from a dict
get_client_id_product_id_charge_options_form_dict = get_client_id_product_id_charge_options.from_dict(get_client_id_product_id_charge_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


