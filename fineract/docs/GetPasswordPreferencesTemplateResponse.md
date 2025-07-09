# GetPasswordPreferencesTemplateResponse

GetPasswordPreferencesTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_password_preferences_template_response import GetPasswordPreferencesTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPasswordPreferencesTemplateResponse from a JSON string
get_password_preferences_template_response_instance = GetPasswordPreferencesTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetPasswordPreferencesTemplateResponse.to_json())

# convert the object into a dict
get_password_preferences_template_response_dict = get_password_preferences_template_response_instance.to_dict()
# create an instance of GetPasswordPreferencesTemplateResponse from a dict
get_password_preferences_template_response_from_dict = GetPasswordPreferencesTemplateResponse.from_dict(get_password_preferences_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


