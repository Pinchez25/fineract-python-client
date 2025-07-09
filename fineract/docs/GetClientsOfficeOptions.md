# GetClientsOfficeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_office_options import GetClientsOfficeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsOfficeOptions from a JSON string
get_clients_office_options_instance = GetClientsOfficeOptions.from_json(json)
# print the JSON string representation of the object
print(GetClientsOfficeOptions.to_json())

# convert the object into a dict
get_clients_office_options_dict = get_clients_office_options_instance.to_dict()
# create an instance of GetClientsOfficeOptions from a dict
get_clients_office_options_from_dict = GetClientsOfficeOptions.from_dict(get_clients_office_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


