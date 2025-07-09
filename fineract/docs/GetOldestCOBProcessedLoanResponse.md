# GetOldestCOBProcessedLoanResponse

GetOldestCOBProcessedLoanResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cob_business_date** | **date** |  | [optional] 
**cob_processed_date** | **date** |  | [optional] 
**loan_ids** | **List[int]** |  | [optional] 

## Example

```python
from fineract_client.models.get_oldest_cob_processed_loan_response import GetOldestCOBProcessedLoanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOldestCOBProcessedLoanResponse from a JSON string
get_oldest_cob_processed_loan_response_instance = GetOldestCOBProcessedLoanResponse.from_json(json)
# print the JSON string representation of the object
print GetOldestCOBProcessedLoanResponse.to_json()

# convert the object into a dict
get_oldest_cob_processed_loan_response_dict = get_oldest_cob_processed_loan_response_instance.to_dict()
# create an instance of GetOldestCOBProcessedLoanResponse from a dict
get_oldest_cob_processed_loan_response_form_dict = get_oldest_cob_processed_loan_response.from_dict(get_oldest_cob_processed_loan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


