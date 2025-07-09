# PagedRequestClientTextSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**request** | [**ClientTextSearch**](ClientTextSearch.md) |  | [optional] 
**size** | **int** |  | [optional] 
**sorts** | [**List[SortOrder]**](SortOrder.md) |  | [optional] 

## Example

```python
from fineract_client.models.paged_request_client_text_search import PagedRequestClientTextSearch

# TODO update the JSON string below
json = "{}"
# create an instance of PagedRequestClientTextSearch from a JSON string
paged_request_client_text_search_instance = PagedRequestClientTextSearch.from_json(json)
# print the JSON string representation of the object
print(PagedRequestClientTextSearch.to_json())

# convert the object into a dict
paged_request_client_text_search_dict = paged_request_client_text_search_instance.to_dict()
# create an instance of PagedRequestClientTextSearch from a dict
paged_request_client_text_search_from_dict = PagedRequestClientTextSearch.from_dict(paged_request_client_text_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


