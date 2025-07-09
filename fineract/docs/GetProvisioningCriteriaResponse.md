# GetProvisioningCriteriaResponse

GetProvisioningCriteriaResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**criteria_id** | **int** |  | [optional] 
**criteria_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_provisioning_criteria_response import GetProvisioningCriteriaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProvisioningCriteriaResponse from a JSON string
get_provisioning_criteria_response_instance = GetProvisioningCriteriaResponse.from_json(json)
# print the JSON string representation of the object
print GetProvisioningCriteriaResponse.to_json()

# convert the object into a dict
get_provisioning_criteria_response_dict = get_provisioning_criteria_response_instance.to_dict()
# create an instance of GetProvisioningCriteriaResponse from a dict
get_provisioning_criteria_response_form_dict = get_provisioning_criteria_response.from_dict(get_provisioning_criteria_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


