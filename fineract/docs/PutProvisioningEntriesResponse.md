# PutProvisioningEntriesResponse

PutProvisioningEntriesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_provisioning_entries_response import PutProvisioningEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutProvisioningEntriesResponse from a JSON string
put_provisioning_entries_response_instance = PutProvisioningEntriesResponse.from_json(json)
# print the JSON string representation of the object
print PutProvisioningEntriesResponse.to_json()

# convert the object into a dict
put_provisioning_entries_response_dict = put_provisioning_entries_response_instance.to_dict()
# create an instance of PutProvisioningEntriesResponse from a dict
put_provisioning_entries_response_form_dict = put_provisioning_entries_response.from_dict(put_provisioning_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


