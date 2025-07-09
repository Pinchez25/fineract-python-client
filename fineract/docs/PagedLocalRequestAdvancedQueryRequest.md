# PagedLocalRequestAdvancedQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**date_time_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**locale_object** | [**PagedLocalRequestAdvancedQueryDataLocaleObject**](PagedLocalRequestAdvancedQueryDataLocaleObject.md) |  | [optional] 
**page** | **int** |  | [optional] 
**request** | [**AdvancedQueryRequest**](AdvancedQueryRequest.md) |  | [optional] 
**size** | **int** |  | [optional] 
**sorts** | [**List[SortOrder]**](SortOrder.md) |  | [optional] 

## Example

```python
from fineract_client.models.paged_local_request_advanced_query_request import PagedLocalRequestAdvancedQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PagedLocalRequestAdvancedQueryRequest from a JSON string
paged_local_request_advanced_query_request_instance = PagedLocalRequestAdvancedQueryRequest.from_json(json)
# print the JSON string representation of the object
print PagedLocalRequestAdvancedQueryRequest.to_json()

# convert the object into a dict
paged_local_request_advanced_query_request_dict = paged_local_request_advanced_query_request_instance.to_dict()
# create an instance of PagedLocalRequestAdvancedQueryRequest from a dict
paged_local_request_advanced_query_request_form_dict = paged_local_request_advanced_query_request.from_dict(paged_local_request_advanced_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


