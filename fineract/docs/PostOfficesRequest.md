# PostOfficesRequest

PostOfficesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**opening_date** | **date** |  | [optional] 
**parent_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_offices_request import PostOfficesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostOfficesRequest from a JSON string
post_offices_request_instance = PostOfficesRequest.from_json(json)
# print the JSON string representation of the object
print PostOfficesRequest.to_json()

# convert the object into a dict
post_offices_request_dict = post_offices_request_instance.to_dict()
# create an instance of PostOfficesRequest from a dict
post_offices_request_form_dict = post_offices_request.from_dict(post_offices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


