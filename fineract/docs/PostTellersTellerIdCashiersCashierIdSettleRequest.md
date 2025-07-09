# PostTellersTellerIdCashiersCashierIdSettleRequest

PostTellersTellerIdCashiersCashierIdSettleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**txn_amount** | **float** |  | [optional] 
**txn_date** | **date** |  | [optional] 
**txn_note** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_tellers_teller_id_cashiers_cashier_id_settle_request import PostTellersTellerIdCashiersCashierIdSettleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTellersTellerIdCashiersCashierIdSettleRequest from a JSON string
post_tellers_teller_id_cashiers_cashier_id_settle_request_instance = PostTellersTellerIdCashiersCashierIdSettleRequest.from_json(json)
# print the JSON string representation of the object
print(PostTellersTellerIdCashiersCashierIdSettleRequest.to_json())

# convert the object into a dict
post_tellers_teller_id_cashiers_cashier_id_settle_request_dict = post_tellers_teller_id_cashiers_cashier_id_settle_request_instance.to_dict()
# create an instance of PostTellersTellerIdCashiersCashierIdSettleRequest from a dict
post_tellers_teller_id_cashiers_cashier_id_settle_request_from_dict = PostTellersTellerIdCashiersCashierIdSettleRequest.from_dict(post_tellers_teller_id_cashiers_cashier_id_settle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


