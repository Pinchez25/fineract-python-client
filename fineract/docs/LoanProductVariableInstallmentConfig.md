# LoanProductVariableInstallmentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**loan_product** | [**LoanProduct**](LoanProduct.md) |  | [optional] 
**maximum_gap** | **int** |  | [optional] 
**minimum_gap** | **int** |  | [optional] 
**new** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_variable_installment_config import LoanProductVariableInstallmentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductVariableInstallmentConfig from a JSON string
loan_product_variable_installment_config_instance = LoanProductVariableInstallmentConfig.from_json(json)
# print the JSON string representation of the object
print LoanProductVariableInstallmentConfig.to_json()

# convert the object into a dict
loan_product_variable_installment_config_dict = loan_product_variable_installment_config_instance.to_dict()
# create an instance of LoanProductVariableInstallmentConfig from a dict
loan_product_variable_installment_config_form_dict = loan_product_variable_installment_config.from_dict(loan_product_variable_installment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


