# PageClientSearchData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[ClientSearchData]**](ClientSearchData.md) |  | [optional] 
**empty** | **bool** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**Pageable**](Pageable.md) |  | [optional] 
**size** | **int** |  | [optional] 
**sort** | [**Sort**](Sort.md) |  | [optional] 
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.page_client_search_data import PageClientSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of PageClientSearchData from a JSON string
page_client_search_data_instance = PageClientSearchData.from_json(json)
# print the JSON string representation of the object
print(PageClientSearchData.to_json())

# convert the object into a dict
page_client_search_data_dict = page_client_search_data_instance.to_dict()
# create an instance of PageClientSearchData from a dict
page_client_search_data_from_dict = PageClientSearchData.from_dict(page_client_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


