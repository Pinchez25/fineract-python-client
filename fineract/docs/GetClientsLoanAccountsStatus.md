# GetClientsLoanAccountsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**closed_obligations_met** | **bool** |  | [optional] 
**closed_rescheduled** | **bool** |  | [optional] 
**closed_written_off** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**overpaid** | **bool** |  | [optional] 
**pending_approval** | **bool** |  | [optional] 
**waiting_for_disbursal** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_loan_accounts_status import GetClientsLoanAccountsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsLoanAccountsStatus from a JSON string
get_clients_loan_accounts_status_instance = GetClientsLoanAccountsStatus.from_json(json)
# print the JSON string representation of the object
print GetClientsLoanAccountsStatus.to_json()

# convert the object into a dict
get_clients_loan_accounts_status_dict = get_clients_loan_accounts_status_instance.to_dict()
# create an instance of GetClientsLoanAccountsStatus from a dict
get_clients_loan_accounts_status_form_dict = get_clients_loan_accounts_status.from_dict(get_clients_loan_accounts_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


