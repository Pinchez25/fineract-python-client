# ColumnFilterData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** |  | [optional] 
**filters** | [**List[FilterData]**](FilterData.md) |  | [optional] 

## Example

```python
from fineract_client.models.column_filter_data import ColumnFilterData

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnFilterData from a JSON string
column_filter_data_instance = ColumnFilterData.from_json(json)
# print the JSON string representation of the object
print ColumnFilterData.to_json()

# convert the object into a dict
column_filter_data_dict = column_filter_data_instance.to_dict()
# create an instance of ColumnFilterData from a dict
column_filter_data_form_dict = column_filter_data.from_dict(column_filter_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


