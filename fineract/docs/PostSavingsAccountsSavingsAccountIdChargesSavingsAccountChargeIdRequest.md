# PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest

PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**date_format** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request import PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest from a JSON string
post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_instance = PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest.from_json(json)
# print the JSON string representation of the object
print(PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest.to_json())

# convert the object into a dict
post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_dict = post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_instance.to_dict()
# create an instance of PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest from a dict
post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_from_dict = PostSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest.from_dict(post_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


