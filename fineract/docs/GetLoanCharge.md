# GetLoanCharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_charge import GetLoanCharge

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanCharge from a JSON string
get_loan_charge_instance = GetLoanCharge.from_json(json)
# print the JSON string representation of the object
print GetLoanCharge.to_json()

# convert the object into a dict
get_loan_charge_dict = get_loan_charge_instance.to_dict()
# create an instance of GetLoanCharge from a dict
get_loan_charge_form_dict = get_loan_charge.from_dict(get_loan_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


