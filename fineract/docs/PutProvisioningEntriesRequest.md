# PutProvisioningEntriesRequest

PutProvisioningEntriesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_provisioning_entries_request import PutProvisioningEntriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutProvisioningEntriesRequest from a JSON string
put_provisioning_entries_request_instance = PutProvisioningEntriesRequest.from_json(json)
# print the JSON string representation of the object
print(PutProvisioningEntriesRequest.to_json())

# convert the object into a dict
put_provisioning_entries_request_dict = put_provisioning_entries_request_instance.to_dict()
# create an instance of PutProvisioningEntriesRequest from a dict
put_provisioning_entries_request_from_dict = PutProvisioningEntriesRequest.from_dict(put_provisioning_entries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


