# GetDelinquencyActionsResponse

GetDelinquencyActionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**created_by_id** | **int** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**end_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**last_modified_on** | **datetime** |  | [optional] 
**start_date** | **date** |  | [optional] 
**updated_by_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_delinquency_actions_response import GetDelinquencyActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDelinquencyActionsResponse from a JSON string
get_delinquency_actions_response_instance = GetDelinquencyActionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDelinquencyActionsResponse.to_json())

# convert the object into a dict
get_delinquency_actions_response_dict = get_delinquency_actions_response_instance.to_dict()
# create an instance of GetDelinquencyActionsResponse from a dict
get_delinquency_actions_response_from_dict = GetDelinquencyActionsResponse.from_dict(get_delinquency_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


