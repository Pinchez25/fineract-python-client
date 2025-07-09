# DeleteProvisioningCriteriaResponse

DeleteProvisioningCriteriaResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_provisioning_criteria_response import DeleteProvisioningCriteriaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteProvisioningCriteriaResponse from a JSON string
delete_provisioning_criteria_response_instance = DeleteProvisioningCriteriaResponse.from_json(json)
# print the JSON string representation of the object
print DeleteProvisioningCriteriaResponse.to_json()

# convert the object into a dict
delete_provisioning_criteria_response_dict = delete_provisioning_criteria_response_instance.to_dict()
# create an instance of DeleteProvisioningCriteriaResponse from a dict
delete_provisioning_criteria_response_form_dict = delete_provisioning_criteria_response.from_dict(delete_provisioning_criteria_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


