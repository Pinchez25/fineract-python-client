# GetLoansResponse

GetLoansResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetLoansLoanIdResponse]**](GetLoansLoanIdResponse.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_response import GetLoansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansResponse from a JSON string
get_loans_response_instance = GetLoansResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoansResponse.to_json())

# convert the object into a dict
get_loans_response_dict = get_loans_response_instance.to_dict()
# create an instance of GetLoansResponse from a dict
get_loans_response_from_dict = GetLoansResponse.from_dict(get_loans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


