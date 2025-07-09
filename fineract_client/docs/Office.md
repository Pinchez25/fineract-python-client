# Office


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[Office]**](Office.md) |  | [optional] 
**external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**opening_date** | **date** |  | [optional] 
**opening_local_date** | **date** |  | [optional] 
**parent** | [**Office**](Office.md) |  | [optional] 

## Example

```python
from fineract_client.models.office import Office

# TODO update the JSON string below
json = "{}"
# create an instance of Office from a JSON string
office_instance = Office.from_json(json)
# print the JSON string representation of the object
print(Office.to_json())

# convert the object into a dict
office_dict = office_instance.to_dict()
# create an instance of Office from a dict
office_from_dict = Office.from_dict(office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


