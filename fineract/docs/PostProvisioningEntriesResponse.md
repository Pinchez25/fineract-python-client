# PostProvisioningEntriesResponse

PostProvisioningEntriesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_provisioning_entries_response import PostProvisioningEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostProvisioningEntriesResponse from a JSON string
post_provisioning_entries_response_instance = PostProvisioningEntriesResponse.from_json(json)
# print the JSON string representation of the object
print PostProvisioningEntriesResponse.to_json()

# convert the object into a dict
post_provisioning_entries_response_dict = post_provisioning_entries_response_instance.to_dict()
# create an instance of PostProvisioningEntriesResponse from a dict
post_provisioning_entries_response_form_dict = post_provisioning_entries_response.from_dict(post_provisioning_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


