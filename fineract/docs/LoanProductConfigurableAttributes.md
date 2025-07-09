# LoanProductConfigurableAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amortization_boolean** | **bool** |  | [optional] 
**amortization_type** | **bool** |  | [optional] 
**arrears_tolerance_boolean** | **bool** |  | [optional] 
**grace_on_arrears_ageing** | **bool** |  | [optional] 
**grace_on_arrears_aging_boolean** | **bool** |  | [optional] 
**grace_on_principal_and_interest_payment** | **bool** |  | [optional] 
**grace_on_principal_and_interest_payment_boolean** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**in_arrears_tolerance** | **bool** |  | [optional] 
**interest_calc_period_boolean** | **bool** |  | [optional] 
**interest_calculation_period_type** | **bool** |  | [optional] 
**interest_method_boolean** | **bool** |  | [optional] 
**interest_type** | **bool** |  | [optional] 
**loan_product** | [**LoanProduct**](LoanProduct.md) |  | [optional] 
**new** | **bool** |  | [optional] 
**repayment_every** | **bool** |  | [optional] 
**repayment_every_boolean** | **bool** |  | [optional] 
**transaction_processing_strategy_boolean** | **bool** |  | [optional] 
**transaction_processing_strategy_code** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_configurable_attributes import LoanProductConfigurableAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductConfigurableAttributes from a JSON string
loan_product_configurable_attributes_instance = LoanProductConfigurableAttributes.from_json(json)
# print the JSON string representation of the object
print LoanProductConfigurableAttributes.to_json()

# convert the object into a dict
loan_product_configurable_attributes_dict = loan_product_configurable_attributes_instance.to_dict()
# create an instance of LoanProductConfigurableAttributes from a dict
loan_product_configurable_attributes_form_dict = loan_product_configurable_attributes.from_dict(loan_product_configurable_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


