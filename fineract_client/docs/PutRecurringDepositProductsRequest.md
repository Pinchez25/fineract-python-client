# PutRecurringDepositProductsRequest

PutRecurringDepositProductsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_recurring_deposit_products_request import PutRecurringDepositProductsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutRecurringDepositProductsRequest from a JSON string
put_recurring_deposit_products_request_instance = PutRecurringDepositProductsRequest.from_json(json)
# print the JSON string representation of the object
print(PutRecurringDepositProductsRequest.to_json())

# convert the object into a dict
put_recurring_deposit_products_request_dict = put_recurring_deposit_products_request_instance.to_dict()
# create an instance of PutRecurringDepositProductsRequest from a dict
put_recurring_deposit_products_request_from_dict = PutRecurringDepositProductsRequest.from_dict(put_recurring_deposit_products_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


