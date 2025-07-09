# LoanProductPaymentAllocationRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_types** | **List[str]** |  | [optional] 
**created_by** | **int** |  | 
**created_date** | **datetime** |  | 
**created_date_time** | **datetime** |  | 
**future_installment_allocation_rule** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | 
**last_modified_date** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**loan_product** | [**LoanProduct**](LoanProduct.md) |  | [optional] 
**new** | **bool** |  | [optional] 
**transaction_type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_payment_allocation_rule import LoanProductPaymentAllocationRule

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductPaymentAllocationRule from a JSON string
loan_product_payment_allocation_rule_instance = LoanProductPaymentAllocationRule.from_json(json)
# print the JSON string representation of the object
print(LoanProductPaymentAllocationRule.to_json())

# convert the object into a dict
loan_product_payment_allocation_rule_dict = loan_product_payment_allocation_rule_instance.to_dict()
# create an instance of LoanProductPaymentAllocationRule from a dict
loan_product_payment_allocation_rule_from_dict = LoanProductPaymentAllocationRule.from_dict(loan_product_payment_allocation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


