# DelSavingsChargeResponse

DeleteSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.del_savings_charge_response import DelSavingsChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DelSavingsChargeResponse from a JSON string
del_savings_charge_response_instance = DelSavingsChargeResponse.from_json(json)
# print the JSON string representation of the object
print(DelSavingsChargeResponse.to_json())

# convert the object into a dict
del_savings_charge_response_dict = del_savings_charge_response_instance.to_dict()
# create an instance of DelSavingsChargeResponse from a dict
del_savings_charge_response_from_dict = DelSavingsChargeResponse.from_dict(del_savings_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


