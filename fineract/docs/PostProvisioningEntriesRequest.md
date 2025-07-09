# PostProvisioningEntriesRequest

PostProvisioningEntriesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createjournalentries** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**entries** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**provisioningentry** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_provisioning_entries_request import PostProvisioningEntriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostProvisioningEntriesRequest from a JSON string
post_provisioning_entries_request_instance = PostProvisioningEntriesRequest.from_json(json)
# print the JSON string representation of the object
print(PostProvisioningEntriesRequest.to_json())

# convert the object into a dict
post_provisioning_entries_request_dict = post_provisioning_entries_request_instance.to_dict()
# create an instance of PostProvisioningEntriesRequest from a dict
post_provisioning_entries_request_from_dict = PostProvisioningEntriesRequest.from_dict(post_provisioning_entries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


