# LoanProductGuaranteeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mandatory_guarantee** | **float** |  | [optional] 
**minimum_guarantee_from_guarantor** | **float** |  | [optional] 
**minimum_guarantee_from_own_funds** | **float** |  | [optional] 
**product_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_guarantee_data import LoanProductGuaranteeData

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductGuaranteeData from a JSON string
loan_product_guarantee_data_instance = LoanProductGuaranteeData.from_json(json)
# print the JSON string representation of the object
print LoanProductGuaranteeData.to_json()

# convert the object into a dict
loan_product_guarantee_data_dict = loan_product_guarantee_data_instance.to_dict()
# create an instance of LoanProductGuaranteeData from a dict
loan_product_guarantee_data_form_dict = loan_product_guarantee_data.from_dict(loan_product_guarantee_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


