# GetSavingsAccountsTemplateResponse

GetSavingsAccountsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**product_options** | [**List[GetSavingsProductOptions]**](GetSavingsProductOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_accounts_template_response import GetSavingsAccountsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAccountsTemplateResponse from a JSON string
get_savings_accounts_template_response_instance = GetSavingsAccountsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetSavingsAccountsTemplateResponse.to_json())

# convert the object into a dict
get_savings_accounts_template_response_dict = get_savings_accounts_template_response_instance.to_dict()
# create an instance of GetSavingsAccountsTemplateResponse from a dict
get_savings_accounts_template_response_from_dict = GetSavingsAccountsTemplateResponse.from_dict(get_savings_accounts_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


