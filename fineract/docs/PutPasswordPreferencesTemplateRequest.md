# PutPasswordPreferencesTemplateRequest

PutPasswordPreferencesTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_policy_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_password_preferences_template_request import PutPasswordPreferencesTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutPasswordPreferencesTemplateRequest from a JSON string
put_password_preferences_template_request_instance = PutPasswordPreferencesTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PutPasswordPreferencesTemplateRequest.to_json())

# convert the object into a dict
put_password_preferences_template_request_dict = put_password_preferences_template_request_instance.to_dict()
# create an instance of PutPasswordPreferencesTemplateRequest from a dict
put_password_preferences_template_request_from_dict = PutPasswordPreferencesTemplateRequest.from_dict(put_password_preferences_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


