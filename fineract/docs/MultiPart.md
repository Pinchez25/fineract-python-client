# MultiPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_parts** | [**List[BodyPart]**](BodyPart.md) |  | [optional] 
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
from fineract_client.models.multi_part import MultiPart

# TODO update the JSON string below
json = "{}"
# create an instance of MultiPart from a JSON string
multi_part_instance = MultiPart.from_json(json)
# print the JSON string representation of the object
print MultiPart.to_json()

# convert the object into a dict
multi_part_dict = multi_part_instance.to_dict()
# create an instance of MultiPart from a dict
multi_part_form_dict = multi_part.from_dict(multi_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


