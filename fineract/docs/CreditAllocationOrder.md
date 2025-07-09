# CreditAllocationOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_allocation_rule** | **str** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.credit_allocation_order import CreditAllocationOrder

# TODO update the JSON string below
json = "{}"
# create an instance of CreditAllocationOrder from a JSON string
credit_allocation_order_instance = CreditAllocationOrder.from_json(json)
# print the JSON string representation of the object
print(CreditAllocationOrder.to_json())

# convert the object into a dict
credit_allocation_order_dict = credit_allocation_order_instance.to_dict()
# create an instance of CreditAllocationOrder from a dict
credit_allocation_order_from_dict = CreditAllocationOrder.from_dict(credit_allocation_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


