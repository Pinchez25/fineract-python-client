# DatatableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registered_table_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.datatable_data import DatatableData

# TODO update the JSON string below
json = "{}"
# create an instance of DatatableData from a JSON string
datatable_data_instance = DatatableData.from_json(json)
# print the JSON string representation of the object
print DatatableData.to_json()

# convert the object into a dict
datatable_data_dict = datatable_data_instance.to_dict()
# create an instance of DatatableData from a dict
datatable_data_form_dict = datatable_data.from_dict(datatable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


