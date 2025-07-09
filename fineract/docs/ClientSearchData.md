# ClientSearchData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**activation_date** | **date** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**display_name** | **str** |  | [optional] 
**external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**id** | **int** |  | [optional] 
**mobile_no** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**status** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.client_search_data import ClientSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSearchData from a JSON string
client_search_data_instance = ClientSearchData.from_json(json)
# print the JSON string representation of the object
print ClientSearchData.to_json()

# convert the object into a dict
client_search_data_dict = client_search_data_instance.to_dict()
# create an instance of ClientSearchData from a dict
client_search_data_form_dict = client_search_data.from_dict(client_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


