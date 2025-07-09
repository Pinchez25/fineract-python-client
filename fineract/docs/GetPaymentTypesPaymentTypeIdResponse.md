# GetPaymentTypesPaymentTypeIdResponse

GetPaymentTypesPaymentTypeIdResponse

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
from fineract_client.models.get_payment_types_payment_type_id_response import GetPaymentTypesPaymentTypeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentTypesPaymentTypeIdResponse from a JSON string
get_payment_types_payment_type_id_response_instance = GetPaymentTypesPaymentTypeIdResponse.from_json(json)
# print the JSON string representation of the object
print GetPaymentTypesPaymentTypeIdResponse.to_json()

# convert the object into a dict
get_payment_types_payment_type_id_response_dict = get_payment_types_payment_type_id_response_instance.to_dict()
# create an instance of GetPaymentTypesPaymentTypeIdResponse from a dict
get_payment_types_payment_type_id_response_form_dict = get_payment_types_payment_type_id_response.from_dict(get_payment_types_payment_type_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


