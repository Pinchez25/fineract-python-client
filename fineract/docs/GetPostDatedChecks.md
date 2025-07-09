# GetPostDatedChecks

GetPostDatedChecks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**var_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**installment_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_post_dated_checks import GetPostDatedChecks

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostDatedChecks from a JSON string
get_post_dated_checks_instance = GetPostDatedChecks.from_json(json)
# print the JSON string representation of the object
print(GetPostDatedChecks.to_json())

# convert the object into a dict
get_post_dated_checks_dict = get_post_dated_checks_instance.to_dict()
# create an instance of GetPostDatedChecks from a dict
get_post_dated_checks_from_dict = GetPostDatedChecks.from_dict(get_post_dated_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


