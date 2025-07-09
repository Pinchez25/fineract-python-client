# LoanTermVariationsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_value** | **date** |  | [optional] 
**decimal_value** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**is_processed** | **bool** |  | [optional] 
**is_specific_to_installment** | **bool** |  | [optional] 
**term_type** | [**LoanTermTypeOptions**](LoanTermTypeOptions.md) |  | [optional] 
**term_variation_applicable_from** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.loan_term_variations_data import LoanTermVariationsData

# TODO update the JSON string below
json = "{}"
# create an instance of LoanTermVariationsData from a JSON string
loan_term_variations_data_instance = LoanTermVariationsData.from_json(json)
# print the JSON string representation of the object
print LoanTermVariationsData.to_json()

# convert the object into a dict
loan_term_variations_data_dict = loan_term_variations_data_instance.to_dict()
# create an instance of LoanTermVariationsData from a dict
loan_term_variations_data_form_dict = loan_term_variations_data.from_dict(loan_term_variations_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


