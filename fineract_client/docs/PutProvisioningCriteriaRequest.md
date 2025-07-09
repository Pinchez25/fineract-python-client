# PutProvisioningCriteriaRequest

PutProvisioningCriteriaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria_name** | **str** |  | [optional] 
**loan_products** | [**List[LoanProductData]**](LoanProductData.md) |  | [optional] 
**provisioningcriteria** | [**List[ProvisioningCriteriaDefinitionData]**](ProvisioningCriteriaDefinitionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.put_provisioning_criteria_request import PutProvisioningCriteriaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutProvisioningCriteriaRequest from a JSON string
put_provisioning_criteria_request_instance = PutProvisioningCriteriaRequest.from_json(json)
# print the JSON string representation of the object
print(PutProvisioningCriteriaRequest.to_json())

# convert the object into a dict
put_provisioning_criteria_request_dict = put_provisioning_criteria_request_instance.to_dict()
# create an instance of PutProvisioningCriteriaRequest from a dict
put_provisioning_criteria_request_from_dict = PutProvisioningCriteriaRequest.from_dict(put_provisioning_criteria_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


