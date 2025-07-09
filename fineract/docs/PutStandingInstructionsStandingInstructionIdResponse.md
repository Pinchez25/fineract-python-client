# PutStandingInstructionsStandingInstructionIdResponse

PutStandingInstructionsStandingInstructionIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutUpdateStandingInstructionChanges**](PutUpdateStandingInstructionChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_standing_instructions_standing_instruction_id_response import PutStandingInstructionsStandingInstructionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutStandingInstructionsStandingInstructionIdResponse from a JSON string
put_standing_instructions_standing_instruction_id_response_instance = PutStandingInstructionsStandingInstructionIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutStandingInstructionsStandingInstructionIdResponse.to_json())

# convert the object into a dict
put_standing_instructions_standing_instruction_id_response_dict = put_standing_instructions_standing_instruction_id_response_instance.to_dict()
# create an instance of PutStandingInstructionsStandingInstructionIdResponse from a dict
put_standing_instructions_standing_instruction_id_response_from_dict = PutStandingInstructionsStandingInstructionIdResponse.from_dict(put_standing_instructions_standing_instruction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


