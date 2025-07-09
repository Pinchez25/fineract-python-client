# GetSelfClientsClientIdResponse

GetSelfClientsClientIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**lastname** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 
**status** | [**GetSelfClientsStatus**](GetSelfClientsStatus.md) |  | [optional] 
**timeline** | [**GetSelfClientsTimeline**](GetSelfClientsTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_client_id_response import GetSelfClientsClientIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsClientIdResponse from a JSON string
get_self_clients_client_id_response_instance = GetSelfClientsClientIdResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfClientsClientIdResponse.to_json()

# convert the object into a dict
get_self_clients_client_id_response_dict = get_self_clients_client_id_response_instance.to_dict()
# create an instance of GetSelfClientsClientIdResponse from a dict
get_self_clients_client_id_response_form_dict = get_self_clients_client_id_response.from_dict(get_self_clients_client_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


