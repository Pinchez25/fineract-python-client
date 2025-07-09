# GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse

GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashier_id** | **int** |  | [optional] 
**cashier_name** | **str** |  | [optional] 
**cashier_transactions** | [**PageCashierTransactionData**](PageCashierTransactionData.md) |  | [optional] 
**net_cash** | **float** |  | [optional] 
**office_name** | **str** |  | [optional] 
**sum_cash_allocation** | **float** |  | [optional] 
**sum_cash_settlement** | **float** |  | [optional] 
**sum_inward_cash** | **float** |  | [optional] 
**sum_outward_cash** | **float** |  | [optional] 
**teller_id** | **int** |  | [optional] 
**teller_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_tellers_teller_id_cashiers_cashiers_id_summary_and_transactions_response import GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse from a JSON string
get_tellers_teller_id_cashiers_cashiers_id_summary_and_transactions_response_instance = GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse.to_json())

# convert the object into a dict
get_tellers_teller_id_cashiers_cashiers_id_summary_and_transactions_response_dict = get_tellers_teller_id_cashiers_cashiers_id_summary_and_transactions_response_instance.to_dict()
# create an instance of GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse from a dict
get_tellers_teller_id_cashiers_cashiers_id_summary_and_transactions_response_from_dict = GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse.from_dict(get_tellers_teller_id_cashiers_cashiers_id_summary_and_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


