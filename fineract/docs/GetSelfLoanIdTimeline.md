# GetSelfLoanIdTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_disbursement_date** | **date** |  | [optional] 
**approved_by_firstname** | **str** |  | [optional] 
**approved_by_lastname** | **str** |  | [optional] 
**approved_by_username** | **str** |  | [optional] 
**approved_on_date** | **date** |  | [optional] 
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
from fineract_client.models.get_self_loan_id_timeline import GetSelfLoanIdTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoanIdTimeline from a JSON string
get_self_loan_id_timeline_instance = GetSelfLoanIdTimeline.from_json(json)
# print the JSON string representation of the object
print GetSelfLoanIdTimeline.to_json()

# convert the object into a dict
get_self_loan_id_timeline_dict = get_self_loan_id_timeline_instance.to_dict()
# create an instance of GetSelfLoanIdTimeline from a dict
get_self_loan_id_timeline_form_dict = get_self_loan_id_timeline.from_dict(get_self_loan_id_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


