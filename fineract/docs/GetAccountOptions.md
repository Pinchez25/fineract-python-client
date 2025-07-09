# GetAccountOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_options import GetAccountOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountOptions from a JSON string
get_account_options_instance = GetAccountOptions.from_json(json)
# print the JSON string representation of the object
print GetAccountOptions.to_json()

# convert the object into a dict
get_account_options_dict = get_account_options_instance.to_dict()
# create an instance of GetAccountOptions from a dict
get_account_options_form_dict = get_account_options.from_dict(get_account_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


