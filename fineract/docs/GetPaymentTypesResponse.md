# GetPaymentTypesResponse

GetPaymentTypesResponse

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
from fineract_client.models.get_payment_types_response import GetPaymentTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentTypesResponse from a JSON string
get_payment_types_response_instance = GetPaymentTypesResponse.from_json(json)
# print the JSON string representation of the object
print(GetPaymentTypesResponse.to_json())

# convert the object into a dict
get_payment_types_response_dict = get_payment_types_response_instance.to_dict()
# create an instance of GetPaymentTypesResponse from a dict
get_payment_types_response_from_dict = GetPaymentTypesResponse.from_dict(get_payment_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


