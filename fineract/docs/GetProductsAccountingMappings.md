# GetProductsAccountingMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**income_from_fee_account_id** | [**GetIncomeFromFeeAccountId**](GetIncomeFromFeeAccountId.md) |  | [optional] 
**share_equity_id** | [**GetShareEquityId**](GetShareEquityId.md) |  | [optional] 
**share_reference_id** | [**GetShareReferenceId**](GetShareReferenceId.md) |  | [optional] 
**share_suspense_id** | [**GetShareSuspenseId**](GetShareSuspenseId.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_products_accounting_mappings import GetProductsAccountingMappings

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsAccountingMappings from a JSON string
get_products_accounting_mappings_instance = GetProductsAccountingMappings.from_json(json)
# print the JSON string representation of the object
print(GetProductsAccountingMappings.to_json())

# convert the object into a dict
get_products_accounting_mappings_dict = get_products_accounting_mappings_instance.to_dict()
# create an instance of GetProductsAccountingMappings from a dict
get_products_accounting_mappings_from_dict = GetProductsAccountingMappings.from_dict(get_products_accounting_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


