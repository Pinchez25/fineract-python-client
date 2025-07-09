# PutSavingsAccountsAccountIdRequest

PutSavingsAccountsAccountIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_savings_accounts_account_id_request import PutSavingsAccountsAccountIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSavingsAccountsAccountIdRequest from a JSON string
put_savings_accounts_account_id_request_instance = PutSavingsAccountsAccountIdRequest.from_json(json)
# print the JSON string representation of the object
print PutSavingsAccountsAccountIdRequest.to_json()

# convert the object into a dict
put_savings_accounts_account_id_request_dict = put_savings_accounts_account_id_request_instance.to_dict()
# create an instance of PutSavingsAccountsAccountIdRequest from a dict
put_savings_accounts_account_id_request_form_dict = put_savings_accounts_account_id_request.from_dict(put_savings_accounts_account_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


