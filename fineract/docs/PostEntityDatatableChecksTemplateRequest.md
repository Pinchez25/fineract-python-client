# PostEntityDatatableChecksTemplateRequest

PostEntityDatatableChecksTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datatable_name** | **str** |  | [optional] 
**entity** | **str** |  | [optional] 
**product_id** | **int** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_entity_datatable_checks_template_request import PostEntityDatatableChecksTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostEntityDatatableChecksTemplateRequest from a JSON string
post_entity_datatable_checks_template_request_instance = PostEntityDatatableChecksTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PostEntityDatatableChecksTemplateRequest.to_json())

# convert the object into a dict
post_entity_datatable_checks_template_request_dict = post_entity_datatable_checks_template_request_instance.to_dict()
# create an instance of PostEntityDatatableChecksTemplateRequest from a dict
post_entity_datatable_checks_template_request_from_dict = PostEntityDatatableChecksTemplateRequest.from_dict(post_entity_datatable_checks_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


