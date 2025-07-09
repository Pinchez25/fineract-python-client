# GetStandingInstructionHistoryPageItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**error_log** | **str** |  | [optional] 
**execution_time** | **date** |  | [optional] 
**from_account** | [**GetStandingInstructionHistoryFromAccount**](GetStandingInstructionHistoryFromAccount.md) |  | [optional] 
**from_account_type** | [**GetFromAccountTypeStandingInstructionSwagger**](GetFromAccountTypeStandingInstructionSwagger.md) |  | [optional] 
**from_client** | [**GetStandingInstructionHistoryPageItemsFromClient**](GetStandingInstructionHistoryPageItemsFromClient.md) |  | [optional] 
**from_office** | [**GetFromOfficeStandingInstructionSwagger**](GetFromOfficeStandingInstructionSwagger.md) |  | [optional] 
**name** | **str** |  | [optional] 
**standing_instruction_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**to_account** | [**GetStandingInstructionHistoryToAccount**](GetStandingInstructionHistoryToAccount.md) |  | [optional] 
**to_account_type** | [**GetToAccountTypeStandingInstructionSwagger**](GetToAccountTypeStandingInstructionSwagger.md) |  | [optional] 
**to_client** | [**GetStandingInstructionHistoryToClient**](GetStandingInstructionHistoryToClient.md) |  | [optional] 
**to_office** | [**GetToOfficeStandingInstructionSwagger**](GetToOfficeStandingInstructionSwagger.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_standing_instruction_history_page_items_response import GetStandingInstructionHistoryPageItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStandingInstructionHistoryPageItemsResponse from a JSON string
get_standing_instruction_history_page_items_response_instance = GetStandingInstructionHistoryPageItemsResponse.from_json(json)
# print the JSON string representation of the object
print(GetStandingInstructionHistoryPageItemsResponse.to_json())

# convert the object into a dict
get_standing_instruction_history_page_items_response_dict = get_standing_instruction_history_page_items_response_instance.to_dict()
# create an instance of GetStandingInstructionHistoryPageItemsResponse from a dict
get_standing_instruction_history_page_items_response_from_dict = GetStandingInstructionHistoryPageItemsResponse.from_dict(get_standing_instruction_history_page_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


