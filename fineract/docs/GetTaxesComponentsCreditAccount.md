# GetTaxesComponentsCreditAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_taxes_components_credit_account import GetTaxesComponentsCreditAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesComponentsCreditAccount from a JSON string
get_taxes_components_credit_account_instance = GetTaxesComponentsCreditAccount.from_json(json)
# print the JSON string representation of the object
print GetTaxesComponentsCreditAccount.to_json()

# convert the object into a dict
get_taxes_components_credit_account_dict = get_taxes_components_credit_account_instance.to_dict()
# create an instance of GetTaxesComponentsCreditAccount from a dict
get_taxes_components_credit_account_form_dict = get_taxes_components_credit_account.from_dict(get_taxes_components_credit_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


