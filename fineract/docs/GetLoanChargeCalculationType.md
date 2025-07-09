# GetLoanChargeCalculationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_charge_calculation_type import GetLoanChargeCalculationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanChargeCalculationType from a JSON string
get_loan_charge_calculation_type_instance = GetLoanChargeCalculationType.from_json(json)
# print the JSON string representation of the object
print GetLoanChargeCalculationType.to_json()

# convert the object into a dict
get_loan_charge_calculation_type_dict = get_loan_charge_calculation_type_instance.to_dict()
# create an instance of GetLoanChargeCalculationType from a dict
get_loan_charge_calculation_type_form_dict = get_loan_charge_calculation_type.from_dict(get_loan_charge_calculation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


