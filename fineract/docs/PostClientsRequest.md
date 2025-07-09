# PostClientsRequest

PostClientsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_date** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**address** | [**List[PostClientsAddressRequest]**](PostClientsAddressRequest.md) | Address requests | [optional] 
**datatables** | [**List[PostClientsDatatable]**](PostClientsDatatable.md) | List of PostClientsDatatable | [optional] 
**date_format** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**email_address** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**group_id** | **int** |  | [optional] 
**lastname** | **str** |  | [optional] 
**legal_form_id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**middlename** | **str** |  | [optional] 
**mobile_no** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_clients_request import PostClientsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsRequest from a JSON string
post_clients_request_instance = PostClientsRequest.from_json(json)
# print the JSON string representation of the object
print(PostClientsRequest.to_json())

# convert the object into a dict
post_clients_request_dict = post_clients_request_instance.to_dict()
# create an instance of PostClientsRequest from a dict
post_clients_request_from_dict = PostClientsRequest.from_dict(post_clients_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


