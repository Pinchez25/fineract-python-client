# PutProvisioningCriteriaResponse

PutProvisioningCriteriaResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutProvisioningCriteriaResponseChanges**](PutProvisioningCriteriaResponseChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_provisioning_criteria_response import PutProvisioningCriteriaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutProvisioningCriteriaResponse from a JSON string
put_provisioning_criteria_response_instance = PutProvisioningCriteriaResponse.from_json(json)
# print the JSON string representation of the object
print PutProvisioningCriteriaResponse.to_json()

# convert the object into a dict
put_provisioning_criteria_response_dict = put_provisioning_criteria_response_instance.to_dict()
# create an instance of PutProvisioningCriteriaResponse from a dict
put_provisioning_criteria_response_form_dict = put_provisioning_criteria_response.from_dict(put_provisioning_criteria_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


