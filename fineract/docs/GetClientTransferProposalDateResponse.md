# GetClientTransferProposalDateResponse

GetClientTransferProposalDateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proposed_transfer_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_client_transfer_proposal_date_response import GetClientTransferProposalDateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientTransferProposalDateResponse from a JSON string
get_client_transfer_proposal_date_response_instance = GetClientTransferProposalDateResponse.from_json(json)
# print the JSON string representation of the object
print GetClientTransferProposalDateResponse.to_json()

# convert the object into a dict
get_client_transfer_proposal_date_response_dict = get_client_transfer_proposal_date_response_instance.to_dict()
# create an instance of GetClientTransferProposalDateResponse from a dict
get_client_transfer_proposal_date_response_form_dict = get_client_transfer_proposal_date_response.from_dict(get_client_transfer_proposal_date_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


