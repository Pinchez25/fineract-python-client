# PostProvisioningCriteriaRequest

PostProvisioningCriteriaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria_name** | **str** |  | [optional] 
**loan_products** | [**List[LoanProductData]**](LoanProductData.md) |  | [optional] 
**provisioningcriteria** | [**List[ProvisioningCriteriaDefinitionData]**](ProvisioningCriteriaDefinitionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.post_provisioning_criteria_request import PostProvisioningCriteriaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostProvisioningCriteriaRequest from a JSON string
post_provisioning_criteria_request_instance = PostProvisioningCriteriaRequest.from_json(json)
# print the JSON string representation of the object
print(PostProvisioningCriteriaRequest.to_json())

# convert the object into a dict
post_provisioning_criteria_request_dict = post_provisioning_criteria_request_instance.to_dict()
# create an instance of PostProvisioningCriteriaRequest from a dict
post_provisioning_criteria_request_from_dict = PostProvisioningCriteriaRequest.from_dict(post_provisioning_criteria_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


