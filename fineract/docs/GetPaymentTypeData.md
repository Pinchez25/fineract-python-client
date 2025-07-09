# GetPaymentTypeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_system_defined** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_payment_type_data import GetPaymentTypeData

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentTypeData from a JSON string
get_payment_type_data_instance = GetPaymentTypeData.from_json(json)
# print the JSON string representation of the object
print(GetPaymentTypeData.to_json())

# convert the object into a dict
get_payment_type_data_dict = get_payment_type_data_instance.to_dict()
# create an instance of GetPaymentTypeData from a dict
get_payment_type_data_from_dict = GetPaymentTypeData.from_dict(get_payment_type_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


