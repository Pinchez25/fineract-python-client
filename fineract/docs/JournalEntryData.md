# JournalEntryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**created_by_user_id** | **int** |  | [optional] 
**created_by_user_name** | **str** |  | [optional] 
**created_date** | **date** |  | [optional] 
**credits** | [**List[CreditDebit]**](CreditDebit.md) |  | [optional] 
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**debits** | [**List[CreditDebit]**](CreditDebit.md) |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**entry_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**gl_account_code** | **str** |  | [optional] 
**gl_account_id** | **int** |  | [optional] 
**gl_account_name** | **str** |  | [optional] 
**gl_account_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**manual_entry** | **bool** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**office_running_balance** | **float** |  | [optional] 
**organization_running_balance** | **float** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**routing_code** | **str** |  | [optional] 
**row_index** | **int** |  | [optional] 
**running_balance_computed** | **bool** |  | [optional] 
**saving_transaction_id** | **int** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**transaction_date** | **date** |  | [optional] 
**transaction_details** | [**TransactionDetailData**](TransactionDetailData.md) |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.journal_entry_data import JournalEntryData

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryData from a JSON string
journal_entry_data_instance = JournalEntryData.from_json(json)
# print the JSON string representation of the object
print(JournalEntryData.to_json())

# convert the object into a dict
journal_entry_data_dict = journal_entry_data_instance.to_dict()
# create an instance of JournalEntryData from a dict
journal_entry_data_from_dict = JournalEntryData.from_dict(journal_entry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


