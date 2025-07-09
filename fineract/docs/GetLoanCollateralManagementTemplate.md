# GetLoanCollateralManagementTemplate

GetLoanCollateralManagementTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_price** | **float** |  | [optional] 
**collateral_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**pct_to_base** | **float** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_collateral_management_template import GetLoanCollateralManagementTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanCollateralManagementTemplate from a JSON string
get_loan_collateral_management_template_instance = GetLoanCollateralManagementTemplate.from_json(json)
# print the JSON string representation of the object
print(GetLoanCollateralManagementTemplate.to_json())

# convert the object into a dict
get_loan_collateral_management_template_dict = get_loan_collateral_management_template_instance.to_dict()
# create an instance of GetLoanCollateralManagementTemplate from a dict
get_loan_collateral_management_template_from_dict = GetLoanCollateralManagementTemplate.from_dict(get_loan_collateral_management_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


