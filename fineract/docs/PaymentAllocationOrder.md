# PaymentAllocationOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | [optional] 
**payment_allocation_rule** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.payment_allocation_order import PaymentAllocationOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAllocationOrder from a JSON string
payment_allocation_order_instance = PaymentAllocationOrder.from_json(json)
# print the JSON string representation of the object
print(PaymentAllocationOrder.to_json())

# convert the object into a dict
payment_allocation_order_dict = payment_allocation_order_instance.to_dict()
# create an instance of PaymentAllocationOrder from a dict
payment_allocation_order_from_dict = PaymentAllocationOrder.from_dict(payment_allocation_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


