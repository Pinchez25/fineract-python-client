# GetLoanProductsLiabilityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_liability_type import GetLoanProductsLiabilityType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsLiabilityType from a JSON string
get_loan_products_liability_type_instance = GetLoanProductsLiabilityType.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsLiabilityType.to_json())

# convert the object into a dict
get_loan_products_liability_type_dict = get_loan_products_liability_type_instance.to_dict()
# create an instance of GetLoanProductsLiabilityType from a dict
get_loan_products_liability_type_from_dict = GetLoanProductsLiabilityType.from_dict(get_loan_products_liability_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


