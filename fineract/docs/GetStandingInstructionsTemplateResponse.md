# GetStandingInstructionsTemplateResponse

GetStandingInstructionsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_account_type** | [**GetFromAccountTypeResponseStandingInstructionSwagger**](GetFromAccountTypeResponseStandingInstructionSwagger.md) |  | [optional] 
**from_account_type_options** | [**List[GetFromAccountTypeOptionsResponseStandingInstructionSwagger]**](GetFromAccountTypeOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**from_client_options** | [**List[GetFromClientOptionsResponseStandingInstructionSwagger]**](GetFromClientOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**from_office** | [**GetFromOfficeResponseStandingInstructionSwagger**](GetFromOfficeResponseStandingInstructionSwagger.md) |  | [optional] 
**from_office_options** | [**List[GetFromOfficeOptionsResponseStandingInstructionSwagger]**](GetFromOfficeOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**instruction_type_options** | [**List[GetInstructionTypeOptionsResponseStandingInstructionSwagger]**](GetInstructionTypeOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**priority_options** | [**List[GetPriorityOptionsResponseStandingInstructionSwagger]**](GetPriorityOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**recurrence_frequency_options** | [**List[GetRecurrenceFrequencyOptionsResponseStandingInstructionSwagger]**](GetRecurrenceFrequencyOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**recurrence_type_options** | [**List[GetRecurrenceTypeOptionsResponseStandingInstructionSwagger]**](GetRecurrenceTypeOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**status_options** | [**List[GetStatusOptionsResponseStandingInstructionSwagger]**](GetStatusOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**to_account_type_options** | [**List[GetToAccountTypeOptionsResponseStandingInstructionSwagger]**](GetToAccountTypeOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**to_office_options** | [**List[GetToOfficeOptionsResponseStandingInstructionSwagger]**](GetToOfficeOptionsResponseStandingInstructionSwagger.md) |  | [optional] 
**transfer_type_options** | [**List[GetTransferTypeOptionsResponseStandingInstructionSwagger]**](GetTransferTypeOptionsResponseStandingInstructionSwagger.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_standing_instructions_template_response import GetStandingInstructionsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStandingInstructionsTemplateResponse from a JSON string
get_standing_instructions_template_response_instance = GetStandingInstructionsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetStandingInstructionsTemplateResponse.to_json()

# convert the object into a dict
get_standing_instructions_template_response_dict = get_standing_instructions_template_response_instance.to_dict()
# create an instance of GetStandingInstructionsTemplateResponse from a dict
get_standing_instructions_template_response_form_dict = get_standing_instructions_template_response.from_dict(get_standing_instructions_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


