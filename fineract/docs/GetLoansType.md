# GetLoansType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**contra** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**disbursement** | **bool** |  | [optional] 
**external_id** | **str** |  | [optional] 
**external_loan_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**recovery_repayment** | **bool** |  | [optional] 
**repayment** | **bool** |  | [optional] 
**repayment_at_disbursement** | **bool** |  | [optional] 
**waive_charges** | **bool** |  | [optional] 
**waive_interest** | **bool** |  | [optional] 
**write_off** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_type import GetLoansType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansType from a JSON string
get_loans_type_instance = GetLoansType.from_json(json)
# print the JSON string representation of the object
print(GetLoansType.to_json())

# convert the object into a dict
get_loans_type_dict = get_loans_type_instance.to_dict()
# create an instance of GetLoansType from a dict
get_loans_type_from_dict = GetLoansType.from_dict(get_loans_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


