# GetTellersTellerIdCashiersCashiersIdTransactionsResponse

GetTellersTellerIdCashiersCashiersIdTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashier_id** | **int** |  | [optional] 
**cashier_name** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**teller_id** | **int** |  | [optional] 
**txn_amount** | **float** |  | [optional] 
**txn_date** | **date** |  | [optional] 
**txn_note** | **str** |  | [optional] 
**txn_type** | [**CashierTxnType**](CashierTxnType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_tellers_teller_id_cashiers_cashiers_id_transactions_response import GetTellersTellerIdCashiersCashiersIdTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTellersTellerIdCashiersCashiersIdTransactionsResponse from a JSON string
get_tellers_teller_id_cashiers_cashiers_id_transactions_response_instance = GetTellersTellerIdCashiersCashiersIdTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print GetTellersTellerIdCashiersCashiersIdTransactionsResponse.to_json()

# convert the object into a dict
get_tellers_teller_id_cashiers_cashiers_id_transactions_response_dict = get_tellers_teller_id_cashiers_cashiers_id_transactions_response_instance.to_dict()
# create an instance of GetTellersTellerIdCashiersCashiersIdTransactionsResponse from a dict
get_tellers_teller_id_cashiers_cashiers_id_transactions_response_form_dict = get_tellers_teller_id_cashiers_cashiers_id_transactions_response.from_dict(get_tellers_teller_id_cashiers_cashiers_id_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


