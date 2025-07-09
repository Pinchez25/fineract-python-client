# PutTemplatesTemplateIdRequest

PutTemplatesTemplateIdRequest

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
from fineract_client.models.put_templates_template_id_request import PutTemplatesTemplateIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutTemplatesTemplateIdRequest from a JSON string
put_templates_template_id_request_instance = PutTemplatesTemplateIdRequest.from_json(json)
# print the JSON string representation of the object
print PutTemplatesTemplateIdRequest.to_json()

# convert the object into a dict
put_templates_template_id_request_dict = put_templates_template_id_request_instance.to_dict()
# create an instance of PutTemplatesTemplateIdRequest from a dict
put_templates_template_id_request_form_dict = put_templates_template_id_request.from_dict(put_templates_template_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


