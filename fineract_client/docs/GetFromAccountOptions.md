# GetFromAccountOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_no** | **int** |  | [optional] 
**account_type** | [**GetAccountOptions**](GetAccountOptions.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_from_account_options import GetFromAccountOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetFromAccountOptions from a JSON string
get_from_account_options_instance = GetFromAccountOptions.from_json(json)
# print the JSON string representation of the object
print(GetFromAccountOptions.to_json())

# convert the object into a dict
get_from_account_options_dict = get_from_account_options_instance.to_dict()
# create an instance of GetFromAccountOptions from a dict
get_from_account_options_from_dict = GetFromAccountOptions.from_dict(get_from_account_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


