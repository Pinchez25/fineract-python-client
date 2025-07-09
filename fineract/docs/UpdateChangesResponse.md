# UpdateChangesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.update_changes_response import UpdateChangesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChangesResponse from a JSON string
update_changes_response_instance = UpdateChangesResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateChangesResponse.to_json())

# convert the object into a dict
update_changes_response_dict = update_changes_response_instance.to_dict()
# create an instance of UpdateChangesResponse from a dict
update_changes_response_from_dict = UpdateChangesResponse.from_dict(update_changes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


