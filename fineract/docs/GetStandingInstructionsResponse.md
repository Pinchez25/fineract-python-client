# GetStandingInstructionsResponse

GetStandingInstructionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetPageItemsStandingInstructionSwagger]**](GetPageItemsStandingInstructionSwagger.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_standing_instructions_response import GetStandingInstructionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStandingInstructionsResponse from a JSON string
get_standing_instructions_response_instance = GetStandingInstructionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetStandingInstructionsResponse.to_json())

# convert the object into a dict
get_standing_instructions_response_dict = get_standing_instructions_response_instance.to_dict()
# create an instance of GetStandingInstructionsResponse from a dict
get_standing_instructions_response_from_dict = GetStandingInstructionsResponse.from_dict(get_standing_instructions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


