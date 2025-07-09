# PostTemplatesRequest

PostTemplatesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**mappers** | [**List[TemplateMapper]**](TemplateMapper.md) |  | [optional] 
**name** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_templates_request import PostTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTemplatesRequest from a JSON string
post_templates_request_instance = PostTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print PostTemplatesRequest.to_json()

# convert the object into a dict
post_templates_request_dict = post_templates_request_instance.to_dict()
# create an instance of PostTemplatesRequest from a dict
post_templates_request_form_dict = post_templates_request.from_dict(post_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


