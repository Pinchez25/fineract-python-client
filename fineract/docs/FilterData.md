# FilterData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from fineract_client.models.filter_data import FilterData

# TODO update the JSON string below
json = "{}"
# create an instance of FilterData from a JSON string
filter_data_instance = FilterData.from_json(json)
# print the JSON string representation of the object
print(FilterData.to_json())

# convert the object into a dict
filter_data_dict = filter_data_instance.to_dict()
# create an instance of FilterData from a dict
filter_data_from_dict = FilterData.from_dict(filter_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


