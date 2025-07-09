# BodyPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_disposition** | [**ContentDisposition**](ContentDisposition.md) |  | [optional] 
**entity** | **object** |  | [optional] 
**headers** | [**BodyPartHeaders**](BodyPartHeaders.md) |  | [optional] 
**media_type** | [**MediaType**](MediaType.md) |  | [optional] 
**message_body_workers** | **object** |  | [optional] 
**parameterized_headers** | [**BodyPartParameterizedHeaders**](BodyPartParameterizedHeaders.md) |  | [optional] 
**parent** | [**MultiPart**](MultiPart.md) |  | [optional] 
**providers** | **object** |  | [optional] 

## Example

```python
from fineract_client.models.body_part import BodyPart

# TODO update the JSON string below
json = "{}"
# create an instance of BodyPart from a JSON string
body_part_instance = BodyPart.from_json(json)
# print the JSON string representation of the object
print BodyPart.to_json()

# convert the object into a dict
body_part_dict = body_part_instance.to_dict()
# create an instance of BodyPart from a dict
body_part_form_dict = body_part.from_dict(body_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


