# GetLoansLoanIdDelinquencyPausePeriod

List of GetLoansLoanIdDelinquencyPausePeriod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**pause_period_end** | **date** |  | [optional] 
**pause_period_start** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_delinquency_pause_period import GetLoansLoanIdDelinquencyPausePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdDelinquencyPausePeriod from a JSON string
get_loans_loan_id_delinquency_pause_period_instance = GetLoansLoanIdDelinquencyPausePeriod.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdDelinquencyPausePeriod.to_json())

# convert the object into a dict
get_loans_loan_id_delinquency_pause_period_dict = get_loans_loan_id_delinquency_pause_period_instance.to_dict()
# create an instance of GetLoansLoanIdDelinquencyPausePeriod from a dict
get_loans_loan_id_delinquency_pause_period_from_dict = GetLoansLoanIdDelinquencyPausePeriod.from_dict(get_loans_loan_id_delinquency_pause_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


