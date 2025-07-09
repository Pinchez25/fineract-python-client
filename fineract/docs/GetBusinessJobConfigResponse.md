# GetBusinessJobConfigResponse

GetBusinessJobConfigResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_jobs** | **List[str]** |  | [optional] 

## Example

```python
from fineract_client.models.get_business_job_config_response import GetBusinessJobConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBusinessJobConfigResponse from a JSON string
get_business_job_config_response_instance = GetBusinessJobConfigResponse.from_json(json)
# print the JSON string representation of the object
print(GetBusinessJobConfigResponse.to_json())

# convert the object into a dict
get_business_job_config_response_dict = get_business_job_config_response_instance.to_dict()
# create an instance of GetBusinessJobConfigResponse from a dict
get_business_job_config_response_from_dict = GetBusinessJobConfigResponse.from_dict(get_business_job_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


