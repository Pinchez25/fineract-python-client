# GetRecurringPaymentDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** |  | [optional] 
**bank_number** | **int** |  | [optional] 
**check_number** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**payment_type** | [**GetRecurringPaymentType**](GetRecurringPaymentType.md) |  | [optional] 
**receipt_number** | **int** |  | [optional] 
**routing_code** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_payment_detail_data import GetRecurringPaymentDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringPaymentDetailData from a JSON string
get_recurring_payment_detail_data_instance = GetRecurringPaymentDetailData.from_json(json)
# print the JSON string representation of the object
print GetRecurringPaymentDetailData.to_json()

# convert the object into a dict
get_recurring_payment_detail_data_dict = get_recurring_payment_detail_data_instance.to_dict()
# create an instance of GetRecurringPaymentDetailData from a dict
get_recurring_payment_detail_data_form_dict = get_recurring_payment_detail_data.from_dict(get_recurring_payment_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


