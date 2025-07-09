# DeleteSavingsChargeResponse

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
from fineract_client.models.delete_savings_charge_response import DeleteSavingsChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSavingsChargeResponse from a JSON string
delete_savings_charge_response_instance = DeleteSavingsChargeResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteSavingsChargeResponse.to_json())

# convert the object into a dict
delete_savings_charge_response_dict = delete_savings_charge_response_instance.to_dict()
# create an instance of DeleteSavingsChargeResponse from a dict
delete_savings_charge_response_from_dict = DeleteSavingsChargeResponse.from_dict(delete_savings_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


