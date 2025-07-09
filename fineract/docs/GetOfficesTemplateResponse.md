# GetOfficesTemplateResponse

GetOfficesTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_parents** | [**List[GetOfficesResponse]**](GetOfficesResponse.md) |  | [optional] 
**opening_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_offices_template_response import GetOfficesTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOfficesTemplateResponse from a JSON string
get_offices_template_response_instance = GetOfficesTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetOfficesTemplateResponse.to_json())

# convert the object into a dict
get_offices_template_response_dict = get_offices_template_response_instance.to_dict()
# create an instance of GetOfficesTemplateResponse from a dict
get_offices_template_response_from_dict = GetOfficesTemplateResponse.from_dict(get_offices_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


