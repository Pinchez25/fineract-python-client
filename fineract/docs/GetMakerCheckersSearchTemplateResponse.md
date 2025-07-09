# GetMakerCheckersSearchTemplateResponse

GetMakerCheckersSearchTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_names** | **List[str]** |  | [optional] 
**app_users** | [**List[AppUserData]**](AppUserData.md) |  | [optional] 
**entity_names** | **List[str]** |  | [optional] 
**processing_results** | [**List[ProcessingResultLookup]**](ProcessingResultLookup.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_maker_checkers_search_template_response import GetMakerCheckersSearchTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMakerCheckersSearchTemplateResponse from a JSON string
get_maker_checkers_search_template_response_instance = GetMakerCheckersSearchTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetMakerCheckersSearchTemplateResponse.to_json()

# convert the object into a dict
get_maker_checkers_search_template_response_dict = get_maker_checkers_search_template_response_instance.to_dict()
# create an instance of GetMakerCheckersSearchTemplateResponse from a dict
get_maker_checkers_search_template_response_form_dict = get_maker_checkers_search_template_response.from_dict(get_maker_checkers_search_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


