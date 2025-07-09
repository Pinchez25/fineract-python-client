# CreditAllocationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_allocation_order** | [**List[CreditAllocationOrder]**](CreditAllocationOrder.md) |  | [optional] 
**transaction_type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.credit_allocation_data import CreditAllocationData

# TODO update the JSON string below
json = "{}"
# create an instance of CreditAllocationData from a JSON string
credit_allocation_data_instance = CreditAllocationData.from_json(json)
# print the JSON string representation of the object
print CreditAllocationData.to_json()

# convert the object into a dict
credit_allocation_data_dict = credit_allocation_data_instance.to_dict()
# create an instance of CreditAllocationData from a dict
credit_allocation_data_form_dict = credit_allocation_data.from_dict(credit_allocation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


