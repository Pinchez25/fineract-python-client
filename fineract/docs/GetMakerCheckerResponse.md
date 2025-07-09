# GetMakerCheckerResponse

GetMakerCheckerResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** |  | [optional] 
**checked_on_date** | **datetime** |  | [optional] 
**checker** | **str** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**command_as_json** | **str** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**group_level_name** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_account_no** | **str** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**made_on_date** | **datetime** |  | [optional] 
**maker** | **str** |  | [optional] 
**office_name** | **str** |  | [optional] 
**processing_result** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_account_no** | **str** |  | [optional] 
**subresource_id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_maker_checker_response import GetMakerCheckerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMakerCheckerResponse from a JSON string
get_maker_checker_response_instance = GetMakerCheckerResponse.from_json(json)
# print the JSON string representation of the object
print GetMakerCheckerResponse.to_json()

# convert the object into a dict
get_maker_checker_response_dict = get_maker_checker_response_instance.to_dict()
# create an instance of GetMakerCheckerResponse from a dict
get_maker_checker_response_form_dict = get_maker_checker_response.from_dict(get_maker_checker_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


