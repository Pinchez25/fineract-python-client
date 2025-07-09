# GetLoanProductsChargeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**amount** | **float** |  | [optional] 
**charge_applies_to** | [**GetLoanProductsChargeAppliesTo**](GetLoanProductsChargeAppliesTo.md) |  | [optional] 
**charge_calculation_type** | [**GetLoanChargeCalculationType**](GetLoanChargeCalculationType.md) |  | [optional] 
**charge_payment_mode** | [**GetLoansChargePaymentMode**](GetLoansChargePaymentMode.md) |  | [optional] 
**charge_time_type** | [**GetLoanChargeTimeType**](GetLoanChargeTimeType.md) |  | [optional] 
**currency** | [**GetLoanProductsCurrencyOptions**](GetLoanProductsCurrencyOptions.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_charge_options import GetLoanProductsChargeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsChargeOptions from a JSON string
get_loan_products_charge_options_instance = GetLoanProductsChargeOptions.from_json(json)
# print the JSON string representation of the object
print GetLoanProductsChargeOptions.to_json()

# convert the object into a dict
get_loan_products_charge_options_dict = get_loan_products_charge_options_instance.to_dict()
# create an instance of GetLoanProductsChargeOptions from a dict
get_loan_products_charge_options_form_dict = get_loan_products_charge_options.from_dict(get_loan_products_charge_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


