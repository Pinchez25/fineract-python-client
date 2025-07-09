# AdvancedPaymentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**future_installment_allocation_rule** | **str** |  | [optional] 
**payment_allocation_order** | [**List[PaymentAllocationOrder]**](PaymentAllocationOrder.md) |  | [optional] 
**transaction_type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.advanced_payment_data import AdvancedPaymentData

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedPaymentData from a JSON string
advanced_payment_data_instance = AdvancedPaymentData.from_json(json)
# print the JSON string representation of the object
print AdvancedPaymentData.to_json()

# convert the object into a dict
advanced_payment_data_dict = advanced_payment_data_instance.to_dict()
# create an instance of AdvancedPaymentData from a dict
advanced_payment_data_form_dict = advanced_payment_data.from_dict(advanced_payment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


