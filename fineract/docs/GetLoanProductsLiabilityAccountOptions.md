# GetLoanProductsLiabilityAccountOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 
**organization_running_balance** | **int** |  | [optional] 
**tag_id** | [**GetLoanProductsLiabilityTagId**](GetLoanProductsLiabilityTagId.md) |  | [optional] 
**type** | [**GetLoanProductsLiabilityType**](GetLoanProductsLiabilityType.md) |  | [optional] 
**usage** | [**GetLoanProductsLiabilityUsage**](GetLoanProductsLiabilityUsage.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_liability_account_options import GetLoanProductsLiabilityAccountOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsLiabilityAccountOptions from a JSON string
get_loan_products_liability_account_options_instance = GetLoanProductsLiabilityAccountOptions.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsLiabilityAccountOptions.to_json())

# convert the object into a dict
get_loan_products_liability_account_options_dict = get_loan_products_liability_account_options_instance.to_dict()
# create an instance of GetLoanProductsLiabilityAccountOptions from a dict
get_loan_products_liability_account_options_from_dict = GetLoanProductsLiabilityAccountOptions.from_dict(get_loan_products_liability_account_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


