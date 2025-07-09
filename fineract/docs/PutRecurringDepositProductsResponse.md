# PutRecurringDepositProductsResponse

PutRecurringDepositProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutRecurringDepositProductsChanges**](PutRecurringDepositProductsChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_recurring_deposit_products_response import PutRecurringDepositProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutRecurringDepositProductsResponse from a JSON string
put_recurring_deposit_products_response_instance = PutRecurringDepositProductsResponse.from_json(json)
# print the JSON string representation of the object
print(PutRecurringDepositProductsResponse.to_json())

# convert the object into a dict
put_recurring_deposit_products_response_dict = put_recurring_deposit_products_response_instance.to_dict()
# create an instance of PutRecurringDepositProductsResponse from a dict
put_recurring_deposit_products_response_from_dict = PutRecurringDepositProductsResponse.from_dict(put_recurring_deposit_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


