# GetLoanProductsLiabilityUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_liability_usage import GetLoanProductsLiabilityUsage

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsLiabilityUsage from a JSON string
get_loan_products_liability_usage_instance = GetLoanProductsLiabilityUsage.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsLiabilityUsage.to_json())

# convert the object into a dict
get_loan_products_liability_usage_dict = get_loan_products_liability_usage_instance.to_dict()
# create an instance of GetLoanProductsLiabilityUsage from a dict
get_loan_products_liability_usage_from_dict = GetLoanProductsLiabilityUsage.from_dict(get_loan_products_liability_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


