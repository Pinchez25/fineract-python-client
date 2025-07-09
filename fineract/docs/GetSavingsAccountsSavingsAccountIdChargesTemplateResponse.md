# GetSavingsAccountsSavingsAccountIdChargesTemplateResponse

GetSavingsAccountsSavingsAccountIdChargesTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_paid** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**amount_written_off** | **float** |  | [optional] 
**charge_options** | [**List[GetSavingsChargesOptions]**](GetSavingsChargesOptions.md) |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_accounts_savings_account_id_charges_template_response import GetSavingsAccountsSavingsAccountIdChargesTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAccountsSavingsAccountIdChargesTemplateResponse from a JSON string
get_savings_accounts_savings_account_id_charges_template_response_instance = GetSavingsAccountsSavingsAccountIdChargesTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetSavingsAccountsSavingsAccountIdChargesTemplateResponse.to_json())

# convert the object into a dict
get_savings_accounts_savings_account_id_charges_template_response_dict = get_savings_accounts_savings_account_id_charges_template_response_instance.to_dict()
# create an instance of GetSavingsAccountsSavingsAccountIdChargesTemplateResponse from a dict
get_savings_accounts_savings_account_id_charges_template_response_from_dict = GetSavingsAccountsSavingsAccountIdChargesTemplateResponse.from_dict(get_savings_accounts_savings_account_id_charges_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


