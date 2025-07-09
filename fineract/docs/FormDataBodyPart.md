# FormDataBodyPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** |  | [optional] 
**content_disposition** | [**ContentDisposition**](ContentDisposition.md) |  | [optional] 
**entity** | **object** |  | [optional] 
**file_name** | **str** |  | [optional] 
**form_data_content_disposition** | [**FormDataContentDisposition**](FormDataContentDisposition.md) |  | [optional] 
**headers** | [**BodyPartHeaders**](BodyPartHeaders.md) |  | [optional] 
**media_type** | [**MediaType**](MediaType.md) |  | [optional] 
**message_body_workers** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**parameterized_headers** | [**BodyPartParameterizedHeaders**](BodyPartParameterizedHeaders.md) |  | [optional] 
**parent** | [**MultiPart**](MultiPart.md) |  | [optional] 
**providers** | **object** |  | [optional] 
**simple** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.form_data_body_part import FormDataBodyPart

# TODO update the JSON string below
json = "{}"
# create an instance of FormDataBodyPart from a JSON string
form_data_body_part_instance = FormDataBodyPart.from_json(json)
# print the JSON string representation of the object
print FormDataBodyPart.to_json()

# convert the object into a dict
form_data_body_part_dict = form_data_body_part_instance.to_dict()
# create an instance of FormDataBodyPart from a dict
form_data_body_part_form_dict = form_data_body_part.from_dict(form_data_body_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


