# GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse

GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashier_data** | [**CashierData**](CashierData.md) |  | [optional] 
**cashier_id** | **int** |  | [optional] 
**cashier_name** | **str** |  | [optional] 
**currency_options** | [**List[CurrencyData]**](CurrencyData.md) |  | [optional] 
**end_date** | **date** |  | [optional] 
**office_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**teller_id** | **int** |  | [optional] 
**teller_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_tellers_teller_id_cashiers_cashiers_id_transactions_template_response import GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse from a JSON string
get_tellers_teller_id_cashiers_cashiers_id_transactions_template_response_instance = GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse.to_json()

# convert the object into a dict
get_tellers_teller_id_cashiers_cashiers_id_transactions_template_response_dict = get_tellers_teller_id_cashiers_cashiers_id_transactions_template_response_instance.to_dict()
# create an instance of GetTellersTellerIdCashiersCashiersIdTransactionsTemplateResponse from a dict
get_tellers_teller_id_cashiers_cashiers_id_transactions_template_response_form_dict = get_tellers_teller_id_cashiers_cashiers_id_transactions_template_response.from_dict(get_tellers_teller_id_cashiers_cashiers_id_transactions_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


