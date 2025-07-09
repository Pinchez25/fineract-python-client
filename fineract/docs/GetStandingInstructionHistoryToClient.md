# GetStandingInstructionHistoryToClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_standing_instruction_history_to_client import GetStandingInstructionHistoryToClient

# TODO update the JSON string below
json = "{}"
# create an instance of GetStandingInstructionHistoryToClient from a JSON string
get_standing_instruction_history_to_client_instance = GetStandingInstructionHistoryToClient.from_json(json)
# print the JSON string representation of the object
print GetStandingInstructionHistoryToClient.to_json()

# convert the object into a dict
get_standing_instruction_history_to_client_dict = get_standing_instruction_history_to_client_instance.to_dict()
# create an instance of GetStandingInstructionHistoryToClient from a dict
get_standing_instruction_history_to_client_form_dict = get_standing_instruction_history_to_client.from_dict(get_standing_instruction_history_to_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


