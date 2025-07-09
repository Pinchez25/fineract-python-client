# GetLoanRescheduleRequestResponse

GetLoanRescheduleRequestResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_account_number** | **str** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**loan_term_variations_data** | [**List[LoanTermVariationsData]**](LoanTermVariationsData.md) |  | [optional] 
**recalculate_interest** | **bool** |  | [optional] 
**reschedule_from_date** | **date** |  | [optional] 
**reschedule_from_installment** | **int** |  | [optional] 
**reschedule_reason_code_value** | [**RescheduleReasonsCodeValue**](RescheduleReasonsCodeValue.md) |  | [optional] 
**reschedule_reason_comment** | **str** |  | [optional] 
**status_enum** | [**GetLoanRescheduleRequestStatus**](GetLoanRescheduleRequestStatus.md) |  | [optional] 
**timeline** | [**RescheduleReasonsTimeline**](RescheduleReasonsTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_reschedule_request_response import GetLoanRescheduleRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanRescheduleRequestResponse from a JSON string
get_loan_reschedule_request_response_instance = GetLoanRescheduleRequestResponse.from_json(json)
# print the JSON string representation of the object
print GetLoanRescheduleRequestResponse.to_json()

# convert the object into a dict
get_loan_reschedule_request_response_dict = get_loan_reschedule_request_response_instance.to_dict()
# create an instance of GetLoanRescheduleRequestResponse from a dict
get_loan_reschedule_request_response_form_dict = get_loan_reschedule_request_response.from_dict(get_loan_reschedule_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


