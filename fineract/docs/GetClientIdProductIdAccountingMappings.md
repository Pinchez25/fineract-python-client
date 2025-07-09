# GetClientIdProductIdAccountingMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_equity_id** | [**GetShareAccountsShareEquityId**](GetShareAccountsShareEquityId.md) |  | [optional] 
**income_from_fee_account_id** | [**GetShareAccountsIncomeFromFeeAccountId**](GetShareAccountsIncomeFromFeeAccountId.md) |  | [optional] 
**share_reference_id** | [**GetShareAccountsShareReferenceId**](GetShareAccountsShareReferenceId.md) |  | [optional] 
**share_suspense_id** | [**GetShareAccountsShareSuspenseId**](GetShareAccountsShareSuspenseId.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_client_id_product_id_accounting_mappings import GetClientIdProductIdAccountingMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientIdProductIdAccountingMappings from a JSON string
get_client_id_product_id_accounting_mappings_instance = GetClientIdProductIdAccountingMappings.from_json(json)
# print the JSON string representation of the object
print(GetClientIdProductIdAccountingMappings.to_json())

# convert the object into a dict
get_client_id_product_id_accounting_mappings_dict = get_client_id_product_id_accounting_mappings_instance.to_dict()
# create an instance of GetClientIdProductIdAccountingMappings from a dict
get_client_id_product_id_accounting_mappings_from_dict = GetClientIdProductIdAccountingMappings.from_dict(get_client_id_product_id_accounting_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


