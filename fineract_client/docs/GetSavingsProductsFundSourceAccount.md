# GetSavingsProductsFundSourceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_fund_source_account import GetSavingsProductsFundSourceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsFundSourceAccount from a JSON string
get_savings_products_fund_source_account_instance = GetSavingsProductsFundSourceAccount.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsFundSourceAccount.to_json())

# convert the object into a dict
get_savings_products_fund_source_account_dict = get_savings_products_fund_source_account_instance.to_dict()
# create an instance of GetSavingsProductsFundSourceAccount from a dict
get_savings_products_fund_source_account_from_dict = GetSavingsProductsFundSourceAccount.from_dict(get_savings_products_fund_source_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


