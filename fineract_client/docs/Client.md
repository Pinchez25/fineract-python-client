# Client


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**account_number_requires_auto_generation** | **bool** |  | [optional] 
**activated_by** | [**AppUser**](AppUser.md) |  | [optional] 
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**client_classification** | [**CodeValue**](CodeValue.md) |  | [optional] 
**client_type** | [**CodeValue**](CodeValue.md) |  | [optional] 
**closed** | **bool** |  | [optional] 
**closed_by** | [**AppUser**](AppUser.md) |  | [optional] 
**closure_date** | **date** |  | [optional] 
**closure_reason** | [**CodeValue**](CodeValue.md) |  | [optional] 
**created_by** | **int** |  | 
**created_date** | **datetime** |  | 
**created_date_time** | **datetime** |  | 
**date_of_birth** | **date** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**firstname** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**gender** | [**CodeValue**](CodeValue.md) |  | [optional] 
**groups** | [**List[Group]**](Group.md) |  | [optional] 
**id** | **int** |  | [optional] 
**identifiers** | [**List[ClientIdentifier]**](ClientIdentifier.md) |  | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**last_modified_by** | **int** |  | 
**last_modified_date** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**lastname** | **str** |  | [optional] 
**legal_form** | **int** |  | [optional] 
**middlename** | **str** |  | [optional] 
**mobile_no** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**not_active** | **bool** |  | [optional] 
**not_pending** | **bool** |  | [optional] 
**not_staff** | **bool** |  | [optional] 
**office** | [**Office**](Office.md) |  | [optional] 
**office_joining_date** | **date** |  | [optional] 
**pending** | **bool** |  | [optional] 
**proposed_transfer_date** | **date** |  | [optional] 
**reactivate_date** | **date** |  | [optional] 
**reactivated_by** | [**AppUser**](AppUser.md) |  | [optional] 
**rejected** | **bool** |  | [optional] 
**rejected_by** | [**AppUser**](AppUser.md) |  | [optional] 
**rejected_date** | **date** |  | [optional] 
**rejection_date** | **date** |  | [optional] 
**rejection_reason** | [**CodeValue**](CodeValue.md) |  | [optional] 
**reopened_by** | [**AppUser**](AppUser.md) |  | [optional] 
**reopened_date** | **date** |  | [optional] 
**savings_account_id** | **int** |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**staff** | [**Staff**](Staff.md) |  | [optional] 
**status** | **int** |  | [optional] 
**sub_status** | [**CodeValue**](CodeValue.md) |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**transfer_in_progress** | **bool** |  | [optional] 
**transfer_in_progress_or_on_hold** | **bool** |  | [optional] 
**transfer_on_hold** | **bool** |  | [optional] 
**transfer_to_office** | [**Office**](Office.md) |  | [optional] 
**withdrawal_date** | **date** |  | [optional] 
**withdrawal_reason** | [**CodeValue**](CodeValue.md) |  | [optional] 
**withdrawn** | **bool** |  | [optional] 
**withdrawn_by** | [**AppUser**](AppUser.md) |  | [optional] 

## Example

```python
from fineract_client.models.client import Client

# TODO update the JSON string below
json = "{}"
# create an instance of Client from a JSON string
client_instance = Client.from_json(json)
# print the JSON string representation of the object
print(Client.to_json())

# convert the object into a dict
client_dict = client_instance.to_dict()
# create an instance of Client from a dict
client_from_dict = Client.from_dict(client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


