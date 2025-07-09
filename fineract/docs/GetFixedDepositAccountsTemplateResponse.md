# GetFixedDepositAccountsTemplateResponse

GetFixedDepositAccountsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**product_options** | [**List[GetFixedDepositAccountsProductOptions]**](GetFixedDepositAccountsProductOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_template_response import GetFixedDepositAccountsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsTemplateResponse from a JSON string
get_fixed_deposit_accounts_template_response_instance = GetFixedDepositAccountsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetFixedDepositAccountsTemplateResponse.to_json()

# convert the object into a dict
get_fixed_deposit_accounts_template_response_dict = get_fixed_deposit_accounts_template_response_instance.to_dict()
# create an instance of GetFixedDepositAccountsTemplateResponse from a dict
get_fixed_deposit_accounts_template_response_form_dict = get_fixed_deposit_accounts_template_response.from_dict(get_fixed_deposit_accounts_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


