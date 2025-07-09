# CommandWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** |  | [optional] 
**cache_resource** | **bool** |  | [optional] 
**client_id** | **int** |  | [optional] 
**command_id** | **int** |  | [optional] 
**create** | **bool** |  | [optional] 
**create_datatable** | **bool** |  | [optional] 
**credit_bureau_id** | **int** |  | [optional] 
**currency_resource** | **bool** |  | [optional] 
**datatable_resource** | **bool** |  | [optional] 
**delete** | **bool** |  | [optional] 
**delete_datatable** | **bool** |  | [optional] 
**delete_multiple** | **bool** |  | [optional] 
**delete_one_to_one** | **bool** |  | [optional] 
**delete_operation** | **bool** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**full_fil_survey** | **bool** |  | [optional] 
**group_id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**job_name** | **str** |  | [optional] 
**var_json** | **str** |  | [optional] 
**loan_disburse_detail_resource** | **bool** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**note_resource** | **bool** |  | [optional] 
**office_id** | **int** |  | [optional] 
**organisation_credit_bureau_id** | **int** |  | [optional] 
**password_preferences_resource** | **bool** |  | [optional] 
**permission_resource** | **bool** |  | [optional] 
**product_id** | **int** |  | [optional] 
**register_datatable** | **bool** |  | [optional] 
**register_survey** | **bool** |  | [optional] 
**savings_id** | **int** |  | [optional] 
**subentity_id** | **int** |  | [optional] 
**survey_resource** | **bool** |  | [optional] 
**task_permission_name** | **str** |  | [optional] 
**template_id** | **int** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**update** | **bool** |  | [optional] 
**update_datatable** | **bool** |  | [optional] 
**update_disbursement_date** | **bool** |  | [optional] 
**update_multiple** | **bool** |  | [optional] 
**update_one_to_one** | **bool** |  | [optional] 
**update_operation** | **bool** |  | [optional] 
**user_resource** | **bool** |  | [optional] 
**working_days_resource** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.command_wrapper import CommandWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CommandWrapper from a JSON string
command_wrapper_instance = CommandWrapper.from_json(json)
# print the JSON string representation of the object
print CommandWrapper.to_json()

# convert the object into a dict
command_wrapper_dict = command_wrapper_instance.to_dict()
# create an instance of CommandWrapper from a dict
command_wrapper_form_dict = command_wrapper.from_dict(command_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


