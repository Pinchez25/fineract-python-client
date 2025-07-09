# PaymentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_system_defined** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.payment_type import PaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentType from a JSON string
payment_type_instance = PaymentType.from_json(json)
# print the JSON string representation of the object
print(PaymentType.to_json())

# convert the object into a dict
payment_type_dict = payment_type_instance.to_dict()
# create an instance of PaymentType from a dict
payment_type_from_dict = PaymentType.from_dict(payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


