# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number_requires_auto_generation** | **bool** |  | [optional] 
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**active_client_members** | [**List[Client]**](Client.md) |  | [optional] 
**center** | **bool** |  | [optional] 
**child_group** | **bool** |  | [optional] 
**client_members** | [**List[Client]**](Client.md) |  | [optional] 
**closed** | **bool** |  | [optional] 
**group** | **bool** |  | [optional] 
**group_level** | [**GroupLevel**](GroupLevel.md) |  | [optional] 
**group_members** | [**List[Group]**](Group.md) |  | [optional] 
**id** | **int** |  | [optional] 
**new** | **bool** |  | [optional] 
**not_active** | **bool** |  | [optional] 
**not_pending** | **bool** |  | [optional] 
**office** | [**Office**](Office.md) |  | [optional] 
**parent** | [**Group**](Group.md) |  | [optional] 
**pending** | **bool** |  | [optional] 
**staff** | [**Staff**](Staff.md) |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**transfer_in_progress** | **bool** |  | [optional] 
**transfer_in_progress_or_on_hold** | **bool** |  | [optional] 
**transfer_on_hold** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print Group.to_json()

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_form_dict = group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


