# GetTaxesComponentsCreditAccountType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_taxes_components_credit_account_type import GetTaxesComponentsCreditAccountType

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesComponentsCreditAccountType from a JSON string
get_taxes_components_credit_account_type_instance = GetTaxesComponentsCreditAccountType.from_json(json)
# print the JSON string representation of the object
print(GetTaxesComponentsCreditAccountType.to_json())

# convert the object into a dict
get_taxes_components_credit_account_type_dict = get_taxes_components_credit_account_type_instance.to_dict()
# create an instance of GetTaxesComponentsCreditAccountType from a dict
get_taxes_components_credit_account_type_from_dict = GetTaxesComponentsCreditAccountType.from_dict(get_taxes_components_credit_account_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


