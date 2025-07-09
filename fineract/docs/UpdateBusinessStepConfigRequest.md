# UpdateBusinessStepConfigRequest

UpdateBusinessStepConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_steps** | [**List[BusinessStep]**](BusinessStep.md) |  | [optional] 

## Example

```python
from fineract_client.models.update_business_step_config_request import UpdateBusinessStepConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBusinessStepConfigRequest from a JSON string
update_business_step_config_request_instance = UpdateBusinessStepConfigRequest.from_json(json)
# print the JSON string representation of the object
print UpdateBusinessStepConfigRequest.to_json()

# convert the object into a dict
update_business_step_config_request_dict = update_business_step_config_request_instance.to_dict()
# create an instance of UpdateBusinessStepConfigRequest from a dict
update_business_step_config_request_form_dict = update_business_step_config_request.from_dict(update_business_step_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


