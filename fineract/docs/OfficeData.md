# OfficeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**external_id** | [**ExternalId**](ExternalId.md) |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 
**opening_date** | **date** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**parent_name** | **str** |  | [optional] 
**row_index** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.office_data import OfficeData

# TODO update the JSON string below
json = "{}"
# create an instance of OfficeData from a JSON string
office_data_instance = OfficeData.from_json(json)
# print the JSON string representation of the object
print(OfficeData.to_json())

# convert the object into a dict
office_data_dict = office_data_instance.to_dict()
# create an instance of OfficeData from a dict
office_data_from_dict = OfficeData.from_dict(office_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


