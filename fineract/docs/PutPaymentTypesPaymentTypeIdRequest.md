# PutPaymentTypesPaymentTypeIdRequest

PutPaymentTypesPaymentTypeIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_cash_payment** | **bool** |  | [optional] 
**is_system_defined** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_payment_types_payment_type_id_request import PutPaymentTypesPaymentTypeIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutPaymentTypesPaymentTypeIdRequest from a JSON string
put_payment_types_payment_type_id_request_instance = PutPaymentTypesPaymentTypeIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutPaymentTypesPaymentTypeIdRequest.to_json())

# convert the object into a dict
put_payment_types_payment_type_id_request_dict = put_payment_types_payment_type_id_request_instance.to_dict()
# create an instance of PutPaymentTypesPaymentTypeIdRequest from a dict
put_payment_types_payment_type_id_request_from_dict = PutPaymentTypesPaymentTypeIdRequest.from_dict(put_payment_types_payment_type_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


