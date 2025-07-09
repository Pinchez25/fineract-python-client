# GetLoanProductsInterestTemplateType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_interest_template_type import GetLoanProductsInterestTemplateType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsInterestTemplateType from a JSON string
get_loan_products_interest_template_type_instance = GetLoanProductsInterestTemplateType.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsInterestTemplateType.to_json())

# convert the object into a dict
get_loan_products_interest_template_type_dict = get_loan_products_interest_template_type_instance.to_dict()
# create an instance of GetLoanProductsInterestTemplateType from a dict
get_loan_products_interest_template_type_from_dict = GetLoanProductsInterestTemplateType.from_dict(get_loan_products_interest_template_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


