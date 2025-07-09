# GetLoansLoanIdChargeTimeType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_charge_time_type import GetLoansLoanIdChargeTimeType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdChargeTimeType from a JSON string
get_loans_loan_id_charge_time_type_instance = GetLoansLoanIdChargeTimeType.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdChargeTimeType.to_json()

# convert the object into a dict
get_loans_loan_id_charge_time_type_dict = get_loans_loan_id_charge_time_type_instance.to_dict()
# create an instance of GetLoansLoanIdChargeTimeType from a dict
get_loans_loan_id_charge_time_type_form_dict = get_loans_loan_id_charge_time_type.from_dict(get_loans_loan_id_charge_time_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


