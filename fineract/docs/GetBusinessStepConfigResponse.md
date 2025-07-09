# GetBusinessStepConfigResponse

GetBusinessStepConfigResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_steps** | [**List[BusinessStep]**](BusinessStep.md) |  | [optional] 
**job_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_business_step_config_response import GetBusinessStepConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessStepConfigResponse from a JSON string
get_business_step_config_response_instance = GetBusinessStepConfigResponse.from_json(json)
# print the JSON string representation of the object
print(GetBusinessStepConfigResponse.to_json())

# convert the object into a dict
get_business_step_config_response_dict = get_business_step_config_response_instance.to_dict()
# create an instance of GetBusinessStepConfigResponse from a dict
get_business_step_config_response_from_dict = GetBusinessStepConfigResponse.from_dict(get_business_step_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


