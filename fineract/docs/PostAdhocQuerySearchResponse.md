# PostAdhocQuerySearchResponse

PostAdhocQuerySearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_out_standing** | **int** |  | [optional] 
**loan_product_name** | **str** |  | [optional] 
**office_name** | **str** |  | [optional] 
**percentage** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_adhoc_query_search_response import PostAdhocQuerySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAdhocQuerySearchResponse from a JSON string
post_adhoc_query_search_response_instance = PostAdhocQuerySearchResponse.from_json(json)
# print the JSON string representation of the object
print PostAdhocQuerySearchResponse.to_json()

# convert the object into a dict
post_adhoc_query_search_response_dict = post_adhoc_query_search_response_instance.to_dict()
# create an instance of PostAdhocQuerySearchResponse from a dict
post_adhoc_query_search_response_form_dict = post_adhoc_query_search_response.from_dict(post_adhoc_query_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


