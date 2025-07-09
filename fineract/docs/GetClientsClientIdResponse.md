# GetClientsClientIdResponse

GetClientsClientIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**groups** | [**List[GetClientsGroups]**](GetClientsGroups.md) |  | [optional] 
**id** | **int** |  | [optional] 
**lastname** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 
**status** | [**GetClientsClientIdStatus**](GetClientsClientIdStatus.md) |  | [optional] 
**timeline** | [**GetClientsTimeline**](GetClientsTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_client_id_response import GetClientsClientIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsClientIdResponse from a JSON string
get_clients_client_id_response_instance = GetClientsClientIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsClientIdResponse.to_json())

# convert the object into a dict
get_clients_client_id_response_dict = get_clients_client_id_response_instance.to_dict()
# create an instance of GetClientsClientIdResponse from a dict
get_clients_client_id_response_from_dict = GetClientsClientIdResponse.from_dict(get_clients_client_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


