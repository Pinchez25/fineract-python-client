# ProvisioningCriteriaDefinitionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 
**expense_account** | **int** |  | [optional] 
**expense_code** | **str** |  | [optional] 
**expense_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**liability_account** | **int** |  | [optional] 
**liability_code** | **str** |  | [optional] 
**liability_name** | **str** |  | [optional] 
**max_age** | **int** |  | [optional] 
**min_age** | **int** |  | [optional] 
**provisioning_percentage** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.provisioning_criteria_definition_data import ProvisioningCriteriaDefinitionData

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningCriteriaDefinitionData from a JSON string
provisioning_criteria_definition_data_instance = ProvisioningCriteriaDefinitionData.from_json(json)
# print the JSON string representation of the object
print ProvisioningCriteriaDefinitionData.to_json()

# convert the object into a dict
provisioning_criteria_definition_data_dict = provisioning_criteria_definition_data_instance.to_dict()
# create an instance of ProvisioningCriteriaDefinitionData from a dict
provisioning_criteria_definition_data_form_dict = provisioning_criteria_definition_data.from_dict(provisioning_criteria_definition_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


