# ClientIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** |  | 
**created_date** | **datetime** |  | 
**created_date_time** | **datetime** |  | 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | 
**last_modified_date** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**new** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.client_identifier import ClientIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIdentifier from a JSON string
client_identifier_instance = ClientIdentifier.from_json(json)
# print the JSON string representation of the object
print(ClientIdentifier.to_json())

# convert the object into a dict
client_identifier_dict = client_identifier_instance.to_dict()
# create an instance of ClientIdentifier from a dict
client_identifier_from_dict = ClientIdentifier.from_dict(client_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


