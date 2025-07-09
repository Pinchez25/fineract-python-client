# LoanTermTypeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.loan_term_type_options import LoanTermTypeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LoanTermTypeOptions from a JSON string
loan_term_type_options_instance = LoanTermTypeOptions.from_json(json)
# print the JSON string representation of the object
print(LoanTermTypeOptions.to_json())

# convert the object into a dict
loan_term_type_options_dict = loan_term_type_options_instance.to_dict()
# create an instance of LoanTermTypeOptions from a dict
loan_term_type_options_from_dict = LoanTermTypeOptions.from_dict(loan_term_type_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


