# GetProvisioningCriteriaCriteriaIdResponse

GetProvisioningCriteriaCriteriaIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**criteria_id** | **int** |  | [optional] 
**criteria_name** | **str** |  | [optional] 
**loan_products** | [**List[LoanProductData]**](LoanProductData.md) |  | [optional] 
**provisioningcriteria** | [**List[ProvisioningCriteriaDefinitionData]**](ProvisioningCriteriaDefinitionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_provisioning_criteria_criteria_id_response import GetProvisioningCriteriaCriteriaIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProvisioningCriteriaCriteriaIdResponse from a JSON string
get_provisioning_criteria_criteria_id_response_instance = GetProvisioningCriteriaCriteriaIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetProvisioningCriteriaCriteriaIdResponse.to_json())

# convert the object into a dict
get_provisioning_criteria_criteria_id_response_dict = get_provisioning_criteria_criteria_id_response_instance.to_dict()
# create an instance of GetProvisioningCriteriaCriteriaIdResponse from a dict
get_provisioning_criteria_criteria_id_response_from_dict = GetProvisioningCriteriaCriteriaIdResponse.from_dict(get_provisioning_criteria_criteria_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


