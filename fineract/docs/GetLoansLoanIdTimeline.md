# GetLoansLoanIdTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_disbursement_date** | **date** |  | [optional] 
**actual_maturity_date** | **date** |  | [optional] 
**approved_by_firstname** | **str** |  | [optional] 
**approved_by_lastname** | **str** |  | [optional] 
**approved_by_username** | **str** |  | [optional] 
**approved_on_date** | **date** |  | [optional] 
**charged_off_by_firstname** | **str** |  | [optional] 
**charged_off_by_lastname** | **str** |  | [optional] 
**charged_off_by_username** | **str** |  | [optional] 
**charged_off_on_date** | **date** |  | [optional] 
**closed_on_date** | **date** |  | [optional] 
**disbursed_by_firstname** | **str** |  | [optional] 
**disbursed_by_lastname** | **str** |  | [optional] 
**disbursed_by_username** | **str** |  | [optional] 
**expected_disbursement_date** | **date** |  | [optional] 
**expected_maturity_date** | **date** |  | [optional] 
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_timeline import GetLoansLoanIdTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdTimeline from a JSON string
get_loans_loan_id_timeline_instance = GetLoansLoanIdTimeline.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdTimeline.to_json()

# convert the object into a dict
get_loans_loan_id_timeline_dict = get_loans_loan_id_timeline_instance.to_dict()
# create an instance of GetLoansLoanIdTimeline from a dict
get_loans_loan_id_timeline_form_dict = get_loans_loan_id_timeline.from_dict(get_loans_loan_id_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


