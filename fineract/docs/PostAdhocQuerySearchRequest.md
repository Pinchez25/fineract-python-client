# PostAdhocQuerySearchRequest

PostAdhocQuerySearchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**include_out_standing_amount_percentage** | **bool** |  | [optional] 
**include_outstanding_amount** | **bool** |  | [optional] 
**loan_date_option** | **str** |  | [optional] 
**loan_from_date** | **date** |  | [optional] 
**loan_to_date** | **date** |  | [optional] 
**locale** | **str** |  | [optional] 
**max_outstanding_amount** | **int** |  | [optional] 
**min_outstanding_amount** | **int** |  | [optional] 
**out_standing_amount_percentage** | **int** |  | [optional] 
**out_standing_amount_percentage_condition** | **str** |  | [optional] 
**outstanding_amount_condition** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_adhoc_query_search_request import PostAdhocQuerySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAdhocQuerySearchRequest from a JSON string
post_adhoc_query_search_request_instance = PostAdhocQuerySearchRequest.from_json(json)
# print the JSON string representation of the object
print PostAdhocQuerySearchRequest.to_json()

# convert the object into a dict
post_adhoc_query_search_request_dict = post_adhoc_query_search_request_instance.to_dict()
# create an instance of PostAdhocQuerySearchRequest from a dict
post_adhoc_query_search_request_form_dict = post_adhoc_query_search_request.from_dict(post_adhoc_query_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


