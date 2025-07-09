# PostSelfBeneficiariesTPTRequest

PostSelfBeneficiariesTPTRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** |  | [optional] 
**account_type** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**office_name** | **str** |  | [optional] 
**transfer_limit** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_beneficiaries_tpt_request import PostSelfBeneficiariesTPTRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfBeneficiariesTPTRequest from a JSON string
post_self_beneficiaries_tpt_request_instance = PostSelfBeneficiariesTPTRequest.from_json(json)
# print the JSON string representation of the object
print(PostSelfBeneficiariesTPTRequest.to_json())

# convert the object into a dict
post_self_beneficiaries_tpt_request_dict = post_self_beneficiaries_tpt_request_instance.to_dict()
# create an instance of PostSelfBeneficiariesTPTRequest from a dict
post_self_beneficiaries_tpt_request_from_dict = PostSelfBeneficiariesTPTRequest.from_dict(post_self_beneficiaries_tpt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


