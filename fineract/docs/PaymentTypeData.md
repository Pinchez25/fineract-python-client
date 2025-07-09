# PaymentTypeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_cash_payment** | **bool** |  | [optional] 
**is_system_defined** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.payment_type_data import PaymentTypeData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypeData from a JSON string
payment_type_data_instance = PaymentTypeData.from_json(json)
# print the JSON string representation of the object
print(PaymentTypeData.to_json())

# convert the object into a dict
payment_type_data_dict = payment_type_data_instance.to_dict()
# create an instance of PaymentTypeData from a dict
payment_type_data_from_dict = PaymentTypeData.from_dict(payment_type_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


