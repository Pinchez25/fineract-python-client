# GetLoanProductsChargeAppliesTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_charge_applies_to import GetLoanProductsChargeAppliesTo

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsChargeAppliesTo from a JSON string
get_loan_products_charge_applies_to_instance = GetLoanProductsChargeAppliesTo.from_json(json)
# print the JSON string representation of the object
print GetLoanProductsChargeAppliesTo.to_json()

# convert the object into a dict
get_loan_products_charge_applies_to_dict = get_loan_products_charge_applies_to_instance.to_dict()
# create an instance of GetLoanProductsChargeAppliesTo from a dict
get_loan_products_charge_applies_to_form_dict = get_loan_products_charge_applies_to.from_dict(get_loan_products_charge_applies_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


