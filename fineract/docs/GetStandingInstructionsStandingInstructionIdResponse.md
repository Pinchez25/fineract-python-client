# GetStandingInstructionsStandingInstructionIdResponse

GetStandingInstructionsStandingInstructionIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_detail_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**from_account** | [**GetFromAccountStandingInstructionSwagger**](GetFromAccountStandingInstructionSwagger.md) |  | [optional] 
**from_account_type** | [**GetFromAccountTypeStandingInstructionSwagger**](GetFromAccountTypeStandingInstructionSwagger.md) |  | [optional] 
**from_client** | [**GetFromClientStandingInstructionSwagger**](GetFromClientStandingInstructionSwagger.md) |  | [optional] 
**from_office** | [**GetFromOfficeStandingInstructionSwagger**](GetFromOfficeStandingInstructionSwagger.md) |  | [optional] 
**id** | **int** |  | [optional] 
**instruction_type** | [**GetInstructionTypeStandingInstructionSwagger**](GetInstructionTypeStandingInstructionSwagger.md) |  | [optional] 
**name** | **str** |  | [optional] 
**priority** | [**GetPriorityStandingInstructionSwagger**](GetPriorityStandingInstructionSwagger.md) |  | [optional] 
**recurrence_frequency** | [**GetRecurrenceFrequencyStandingInstructionSwagger**](GetRecurrenceFrequencyStandingInstructionSwagger.md) |  | [optional] 
**recurrence_interval** | **int** |  | [optional] 
**recurrence_on_month_day** | **date** |  | [optional] 
**recurrence_type** | [**GetRecurrenceTypeStandingInstructionSwagger**](GetRecurrenceTypeStandingInstructionSwagger.md) |  | [optional] 
**status** | [**GetStatusStandingInstructionSwagger**](GetStatusStandingInstructionSwagger.md) |  | [optional] 
**to_account** | [**GetToAccountStandingInstructionSwagger**](GetToAccountStandingInstructionSwagger.md) |  | [optional] 
**to_account_type** | [**GetToAccountTypeStandingInstructionSwagger**](GetToAccountTypeStandingInstructionSwagger.md) |  | [optional] 
**to_client** | [**GetToClientStandingInstructionSwagger**](GetToClientStandingInstructionSwagger.md) |  | [optional] 
**to_office** | [**GetToOfficeStandingInstructionSwagger**](GetToOfficeStandingInstructionSwagger.md) |  | [optional] 
**transfer_type** | [**GetTransferTypeStandingInstructionSwagger**](GetTransferTypeStandingInstructionSwagger.md) |  | [optional] 
**valid_from** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_standing_instructions_standing_instruction_id_response import GetStandingInstructionsStandingInstructionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStandingInstructionsStandingInstructionIdResponse from a JSON string
get_standing_instructions_standing_instruction_id_response_instance = GetStandingInstructionsStandingInstructionIdResponse.from_json(json)
# print the JSON string representation of the object
print GetStandingInstructionsStandingInstructionIdResponse.to_json()

# convert the object into a dict
get_standing_instructions_standing_instruction_id_response_dict = get_standing_instructions_standing_instruction_id_response_instance.to_dict()
# create an instance of GetStandingInstructionsStandingInstructionIdResponse from a dict
get_standing_instructions_standing_instruction_id_response_form_dict = get_standing_instructions_standing_instruction_id_response.from_dict(get_standing_instructions_standing_instruction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


