# GetStandingInstructionRunHistoryResponse

GetStandingInstructionRunHistoryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetStandingInstructionHistoryPageItemsResponse]**](GetStandingInstructionHistoryPageItemsResponse.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_standing_instruction_run_history_response import GetStandingInstructionRunHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStandingInstructionRunHistoryResponse from a JSON string
get_standing_instruction_run_history_response_instance = GetStandingInstructionRunHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(GetStandingInstructionRunHistoryResponse.to_json())

# convert the object into a dict
get_standing_instruction_run_history_response_dict = get_standing_instruction_run_history_response_instance.to_dict()
# create an instance of GetStandingInstructionRunHistoryResponse from a dict
get_standing_instruction_run_history_response_from_dict = GetStandingInstructionRunHistoryResponse.from_dict(get_standing_instruction_run_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


