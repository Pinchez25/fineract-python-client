# GetDelinquencyTagHistoryResponse

GetDelinquencyTagHistoryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_on_date** | **date** |  | [optional] 
**delinquency_range** | [**GetDelinquencyRangesResponse**](GetDelinquencyRangesResponse.md) |  | [optional] 
**id** | **int** |  | [optional] 
**lifted_on_date** | **date** |  | [optional] 
**loan_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_delinquency_tag_history_response import GetDelinquencyTagHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDelinquencyTagHistoryResponse from a JSON string
get_delinquency_tag_history_response_instance = GetDelinquencyTagHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(GetDelinquencyTagHistoryResponse.to_json())

# convert the object into a dict
get_delinquency_tag_history_response_dict = get_delinquency_tag_history_response_instance.to_dict()
# create an instance of GetDelinquencyTagHistoryResponse from a dict
get_delinquency_tag_history_response_from_dict = GetDelinquencyTagHistoryResponse.from_dict(get_delinquency_tag_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


