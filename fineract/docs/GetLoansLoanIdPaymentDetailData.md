# GetLoansLoanIdPaymentDetailData

Payment detail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**payment_type** | [**GetLoansLoanIdPaymentType**](GetLoansLoanIdPaymentType.md) |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**routing_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_payment_detail_data import GetLoansLoanIdPaymentDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdPaymentDetailData from a JSON string
get_loans_loan_id_payment_detail_data_instance = GetLoansLoanIdPaymentDetailData.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdPaymentDetailData.to_json())

# convert the object into a dict
get_loans_loan_id_payment_detail_data_dict = get_loans_loan_id_payment_detail_data_instance.to_dict()
# create an instance of GetLoansLoanIdPaymentDetailData from a dict
get_loans_loan_id_payment_detail_data_from_dict = GetLoansLoanIdPaymentDetailData.from_dict(get_loans_loan_id_payment_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


