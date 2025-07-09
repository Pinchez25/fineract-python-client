# TemplateMapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mapperkey** | **str** |  | [optional] 
**mapperorder** | **int** |  | [optional] 
**mappervalue** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.template_mapper import TemplateMapper

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateMapper from a JSON string
template_mapper_instance = TemplateMapper.from_json(json)
# print the JSON string representation of the object
print(TemplateMapper.to_json())

# convert the object into a dict
template_mapper_dict = template_mapper_instance.to_dict()
# create an instance of TemplateMapper from a dict
template_mapper_from_dict = TemplateMapper.from_dict(template_mapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


