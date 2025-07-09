# PaymentDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**payment_type** | [**PaymentType**](PaymentType.md) |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**routing_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.payment_detail_data import PaymentDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetailData from a JSON string
payment_detail_data_instance = PaymentDetailData.from_json(json)
# print the JSON string representation of the object
print(PaymentDetailData.to_json())

# convert the object into a dict
payment_detail_data_dict = payment_detail_data_instance.to_dict()
# create an instance of PaymentDetailData from a dict
payment_detail_data_from_dict = PaymentDetailData.from_dict(payment_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


