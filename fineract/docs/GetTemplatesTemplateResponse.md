# GetTemplatesTemplateResponse

GetTemplatesTemplateResponse

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
from fineract_client.models.get_templates_template_response import GetTemplatesTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplatesTemplateResponse from a JSON string
get_templates_template_response_instance = GetTemplatesTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetTemplatesTemplateResponse.to_json()

# convert the object into a dict
get_templates_template_response_dict = get_templates_template_response_instance.to_dict()
# create an instance of GetTemplatesTemplateResponse from a dict
get_templates_template_response_form_dict = get_templates_template_response.from_dict(get_templates_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


