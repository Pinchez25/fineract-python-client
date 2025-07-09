# ClientFamilyMembersData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**gender_id** | **int** |  | [optional] 
**gender_id_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**id** | **int** |  | [optional] 
**is_dependent** | **bool** |  | [optional] 
**last_name** | **str** |  | [optional] 
**marital_status** | **str** |  | [optional] 
**marital_status_id** | **int** |  | [optional] 
**marital_status_id_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**profession** | **str** |  | [optional] 
**profession_id** | **int** |  | [optional] 
**profession_id_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**qualification** | **str** |  | [optional] 
**relationship** | **str** |  | [optional] 
**relationship_id** | **int** |  | [optional] 
**relationship_id_options** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 

## Example

```python
from fineract_client.models.client_family_members_data import ClientFamilyMembersData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFamilyMembersData from a JSON string
client_family_members_data_instance = ClientFamilyMembersData.from_json(json)
# print the JSON string representation of the object
print(ClientFamilyMembersData.to_json())

# convert the object into a dict
client_family_members_data_dict = client_family_members_data_instance.to_dict()
# create an instance of ClientFamilyMembersData from a dict
client_family_members_data_from_dict = ClientFamilyMembersData.from_dict(client_family_members_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


