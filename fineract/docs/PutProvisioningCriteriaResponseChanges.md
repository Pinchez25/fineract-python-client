# PutProvisioningCriteriaResponseChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_provisioning_criteria_response_changes import PutProvisioningCriteriaResponseChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutProvisioningCriteriaResponseChanges from a JSON string
put_provisioning_criteria_response_changes_instance = PutProvisioningCriteriaResponseChanges.from_json(json)
# print the JSON string representation of the object
print(PutProvisioningCriteriaResponseChanges.to_json())

# convert the object into a dict
put_provisioning_criteria_response_changes_dict = put_provisioning_criteria_response_changes_instance.to_dict()
# create an instance of PutProvisioningCriteriaResponseChanges from a dict
put_provisioning_criteria_response_changes_from_dict = PutProvisioningCriteriaResponseChanges.from_dict(put_provisioning_criteria_response_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


