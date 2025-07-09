# GetSavingsAccountTransactionsPageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_no** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**charges_paid_by_data** | [**List[GetSavingsAccountChargesPaidByData]**](GetSavingsAccountChargesPaidByData.md) |  | [optional] 
**currency** | [**GetTransactionsCurrency**](GetTransactionsCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**entry_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interested_posted_as_on** | **bool** |  | [optional] 
**is_manual_transaction** | **bool** |  | [optional] 
**is_reversal** | **bool** |  | [optional] 
**lien_transaction** | **bool** |  | [optional] 
**original_transaction_id** | **int** |  | [optional] 
**payment_detail_data** | [**GetTransactionsPaymentDetailData**](GetTransactionsPaymentDetailData.md) |  | [optional] 
**release_transaction_id** | **int** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**running_balance** | **float** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**transaction_type** | [**GetTranscationEnumData**](GetTranscationEnumData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_account_transactions_page_item import GetSavingsAccountTransactionsPageItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAccountTransactionsPageItem from a JSON string
get_savings_account_transactions_page_item_instance = GetSavingsAccountTransactionsPageItem.from_json(json)
# print the JSON string representation of the object
print GetSavingsAccountTransactionsPageItem.to_json()

# convert the object into a dict
get_savings_account_transactions_page_item_dict = get_savings_account_transactions_page_item_instance.to_dict()
# create an instance of GetSavingsAccountTransactionsPageItem from a dict
get_savings_account_transactions_page_item_form_dict = get_savings_account_transactions_page_item.from_dict(get_savings_account_transactions_page_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


