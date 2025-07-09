# PagedLocalRequestAdvancedQueryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**date_time_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**locale_object** | [**PagedLocalRequestAdvancedQueryDataLocaleObject**](PagedLocalRequestAdvancedQueryDataLocaleObject.md) |  | [optional] 
**page** | **int** |  | [optional] 
**request** | [**AdvancedQueryData**](AdvancedQueryData.md) |  | [optional] 
**size** | **int** |  | [optional] 
**sorts** | [**List[SortOrder]**](SortOrder.md) |  | [optional] 

## Example

```python
from fineract_client.models.paged_local_request_advanced_query_data import PagedLocalRequestAdvancedQueryData

# TODO update the JSON string below
json = "{}"
# create an instance of PagedLocalRequestAdvancedQueryData from a JSON string
paged_local_request_advanced_query_data_instance = PagedLocalRequestAdvancedQueryData.from_json(json)
# print the JSON string representation of the object
print(PagedLocalRequestAdvancedQueryData.to_json())

# convert the object into a dict
paged_local_request_advanced_query_data_dict = paged_local_request_advanced_query_data_instance.to_dict()
# create an instance of PagedLocalRequestAdvancedQueryData from a dict
paged_local_request_advanced_query_data_from_dict = PagedLocalRequestAdvancedQueryData.from_dict(paged_local_request_advanced_query_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


